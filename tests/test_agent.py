import pytest
from src.crop_engine import PrecisionAgriEngine

def test_ndvi_calculation():
    engine = PrecisionAgriEngine()
    res = engine.compute_ndvi(0.70, 0.20)
    # (0.7 - 0.2) / (0.7 + 0.2) = 0.556
    assert res["ndvi_index"] == 0.556
    assert res["crop_health_status"] == "MODERATE_STRESS"

def test_fertilizer_deficit():
    engine = PrecisionAgriEngine()
    res = engine.calculate_npk_fertilizer(current_n=30, current_p=10, current_k=40, target_yield_tons=5.0)
    assert res["nitrogen_deficit_kg_ha"] == 90.0
