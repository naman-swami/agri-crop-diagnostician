"""
Agronomic Soil Stoichiometry & Nutrient Amendment
Calculates crop NPK uptake deficits and prescriptive Urea / DAP fertilizer blending.
"""
from typing import Dict, Any

class SoilNutrientEngine:
    @staticmethod
    def calculate_npk_prescription(
        current_n: float,
        current_p: float,
        current_k: float,
        target_yield_tons: float
    ) -> Dict[str, Any]:
        # Uptake requirements per ton of grain yield
        req_n = target_yield_tons * 24.0
        req_p = target_yield_tons * 8.5
        req_k = target_yield_tons * 18.0

        def_n = max(0.0, req_n - current_n)
        def_p = max(0.0, req_p - current_p)
        def_k = max(0.0, req_k - current_k)

        # Fertilizer conversion (Urea 46% N; DAP 18% N, 46% P2O5; MOP 60% K2O)
        dap_req = round(def_p / 0.46, 1)
        n_from_dap = dap_req * 0.18
        remaining_n = max(0.0, def_n - n_from_dap)
        urea_req = round(remaining_n / 0.46, 1)
        mop_req = round(def_k / 0.60, 1)

        return {
            "deficits_kg_ha": {"nitrogen": round(def_n, 1), "phosphorus": round(def_p, 1), "potassium": round(def_k, 1)},
            "prescriptive_blend_kg_ha": {"urea": urea_req, "dap": dap_req, "mop": mop_req},
            "recommendation": f"Apply {urea_req} kg/ha Urea, {dap_req} kg/ha DAP, and {mop_req} kg/ha MOP."
        }
