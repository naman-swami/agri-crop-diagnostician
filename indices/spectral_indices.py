"""
Multispectral Remote Sensing Indices
Calculates Normalized Difference Vegetation Index (NDVI) and Normalized Difference Water Index (NDWI).
"""
from typing import Dict, Any

class SpectralIndexCalculator:
    @staticmethod
    def calculate_ndvi(nir: float, red: float) -> Dict[str, Any]:
        denom = nir + red
        if denom == 0:
            ndvi = 0.0
        else:
            ndvi = round((nir - red) / denom, 3)

        if ndvi >= 0.65:
            canopy = "DENSE_VIGOROUS_CANOPY"
            health = "HEALTHY"
        elif ndvi >= 0.35:
            canopy = "MODERATE_CANOPY"
            health = "STRESSED"
        else:
            canopy = "SPARSE_CHLOROTIC_CANOPY"
            health = "SEVERE_STRESS_OR_BARE_SOIL"

        return {
            "ndvi": ndvi,
            "canopy_density": canopy,
            "health_status": health
        }

    @staticmethod
    def calculate_ndwi(nir: float, swir: float) -> Dict[str, Any]:
        denom = nir + swir
        ndwi = 0.0 if denom == 0 else round((nir - swir) / denom, 3)
        water_stress = "ADEQUATE_CANOPY_HYDRATION" if ndwi >= 0.30 else "WATER_DEFICIT_IRRIGATION_NEEDED"
        return {
            "ndwi": ndwi,
            "water_status": water_stress
        }
