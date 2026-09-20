import json
import argparse
from src.crop_engine import PrecisionAgriEngine

def main():
    parser = argparse.ArgumentParser(description="AgriCrop Precision Diagnostic CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated foliar pathology and soil nutrient audit")
    args = parser.parse_args()

    engine = PrecisionAgriEngine()
    ndvi_report = engine.compute_ndvi(nir_reflectance=0.62, red_reflectance=0.18)
    npk_report = engine.calculate_npk_fertilizer(current_n=45.0, current_p=12.0, current_k=65.0, target_yield_tons=6.5)

    report = {"spectral_analysis": ndvi_report, "nutrient_amendment": npk_report}
    print("="*60)
    print(" AGRISHIELD PRECISION CROP AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
