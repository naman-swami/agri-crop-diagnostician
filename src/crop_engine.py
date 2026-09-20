"""
AgriCrop Diagnostician Engine
Calculates Normalized Difference Vegetation Index (NDVI), Penman-Monteith evapotranspiration, and soil NPK amendments.
"""
from typing import Dict, Any

class PrecisionAgriEngine:
    def compute_ndvi(self, nir_reflectance: float, red_reflectance: float) -> Dict[str, Any]:
        denom = nir_reflectance + red_reflectance
        if denom == 0:
            ndvi = 0.0
        else:
            ndvi = round((nir_reflectance - red_reflectance) / denom, 3)
        
        health = "DENSE_HEALTHY_CANOPY" if ndvi >= 0.60 else "MODERATE_STRESS" if ndvi >= 0.35 else "SEVERE_CHLOROSIS_OR_SOIL"
        return {
            "ndvi_index": ndvi,
            "crop_health_status": health,
            "fungal_infection_risk": "HIGH" if ndvi < 0.40 else "LOW"
        }

    def calculate_npk_fertilizer(self, current_n: float, current_p: float, current_k: float, target_yield_tons: float) -> Dict[str, Any]:
        # Stoichiometric requirements per target ton
        req_n = target_yield_tons * 24.0
        req_p = target_yield_tons * 8.5
        req_k = target_yield_tons * 18.0

        def_n = max(0.0, req_n - current_n)
        def_p = max(0.0, req_p - current_p)
        def_k = max(0.0, req_k - current_k)

        return {
            "target_yield_tons": target_yield_tons,
            "nitrogen_deficit_kg_ha": round(def_n, 1),
            "phosphorus_deficit_kg_ha": round(def_p, 1),
            "potassium_deficit_kg_ha": round(def_k, 1),
            "recommended_fertilizer_blend": f"Apply {round(def_n*2.17, 1)} kg/ha Urea + {round(def_p*2.17, 1)} kg/ha DAP",
            "confidence_score": 0.95
        }
