import argparse
import json
import os
from indices.spectral_indices import SpectralIndexCalculator
from agronomy.fertilizer_stoichiometry import SoilNutrientEngine

def main():
    parser = argparse.ArgumentParser(description="AgriCrop Precision Diagnostics CLI")
    parser.add_argument("--demo", action="store_true", help="Audit sample drone field survey")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "field_surveys", "sample_field_data.json")

    if args.demo:
        with open(data_file, "r") as f:
            plots = json.load(f)
        print("=== AGRICROP PRECISION FOLIAR & SOIL DIAGNOSTIC REPORT ===\n")
        for p in plots:
            ndvi_res = SpectralIndexCalculator.calculate_ndvi(p["nir"], p["red"])
            ndwi_res = SpectralIndexCalculator.calculate_ndwi(p["nir"], p["swir"])
            fert_res = SoilNutrientEngine.calculate_npk_prescription(
                p["soil_n_kg_ha"], p["soil_p_kg_ha"], p["soil_k_kg_ha"], p["target_yield_t_ha"]
            )
            print(f"Plot: {p['plot_id']} ({p['crop']}) | Target Yield: {p['target_yield_t_ha']} t/ha")
            print(f"  NDVI: {ndvi_res['ndvi']} ({ndvi_res['health_status']}) | NDWI: {ndwi_res['ndwi']} ({ndwi_res['water_status']})")
            print(f"  Nutrient Deficits: N={fert_res['deficits_kg_ha']['nitrogen']}kg, P={fert_res['deficits_kg_ha']['phosphorus']}kg, K={fert_res['deficits_kg_ha']['potassium']}kg")
            print(f"  Prescription: {fert_res['recommendation']}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
