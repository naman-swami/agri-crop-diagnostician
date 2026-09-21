import os
import pytest
from indices.spectral_indices import SpectralIndexCalculator
from agronomy.fertilizer_stoichiometry import SoilNutrientEngine

def test_ndvi_vigorous_canopy():
    res = SpectralIndexCalculator.calculate_ndvi(nir=0.75, red=0.15)
    assert res["ndvi"] == 0.667
    assert res["health_status"] == "HEALTHY"

def test_ndwi_water_stress():
    res = SpectralIndexCalculator.calculate_ndwi(nir=0.40, swir=0.40)
    assert res["ndwi"] == 0.0
    assert res["water_status"] == "WATER_DEFICIT_IRRIGATION_NEEDED"

def test_fertilizer_prescription():
    res = SoilNutrientEngine.calculate_npk_prescription(
        current_n=50.0, current_p=20.0, current_k=50.0, target_yield_tons=5.0
    )
    assert res["deficits_kg_ha"]["nitrogen"] == 70.0 # 5*24 - 50 = 70
    assert res["prescriptive_blend_kg_ha"]["urea"] > 0
    assert res["prescriptive_blend_kg_ha"]["dap"] > 0
