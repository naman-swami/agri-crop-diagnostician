# Agri Crop Diagnostician & Agronomy Oracle

> **Precision Agriculture Engine: Multispectral Canopy Indices & Soil Stoichiometry**  
> Calculating NDVI/NDWI Vegetation Stress and Computing Precise NPK Fertilizer Prescriptions.

---

### Remote Sensing Spectral Formulations

Canopy indices are calculated from Sentinel-2 / Landsat multispectral reflectance bands:

$$NDVI = \frac{NIR - RED}{NIR + RED} \quad \left(\text{Healthy Vigorous Vegetation: } 0.60 - 0.90\right)$$
$$NDWI = \frac{NIR - SWIR}{NIR + SWIR} \quad \left(\text{Canopy Water Deficit: } < 0.20\right)$$

---

### Soil Stoichiometric Amendment Engine

Fertilizer prescriptions (`agronomy/fertilizer_stoichiometry.py`) reconcile soil nutrient deficiencies against crop-specific uptake targets:

| Fertilizer Carrier | Active Nutrient Content | Calculation Formulation |
| :--- | :--- | :--- |
| **Urea** | $46\% \text{ Nitrogen } (N)$ | $\text{Urea (kg/ha)} = \frac{\Delta N}{0.46}$ |
| **Diammonium Phosphate (DAP)** | $18\% N, 46\% P_2O_5$ | $\text{DAP (kg/ha)} = \frac{\Delta P_2O_5}{0.46}$ |
| **Muriate of Potash (MOP)** | $60\% K_2O$ | $\text{MOP (kg/ha)} = \frac{\Delta K_2O}{0.60}$ |

---

### Field Survey Diagnostic Output

```console
$ python diagnose.py --demo
============================================================
AGRONOMIC FIELD DIAGNOSTIC REPORT: Parcel #NE-402
Crop: Zea mays (Maize) | Growth Stage: V6 Vegetative
============================================================
* Measured NDVI: 0.38 (Severe Chlorosis / Canopy Stunting)
* Measured NDWI: 0.12 (Moderate Water Stress)
* Soil Nitrogen Deficit: 45.0 kg N / hectare
* Prescribed Amendment:
  - Apply 97.8 kg/ha Urea via split side-dressing
  - Schedule 35mm drip irrigation cycle within 48 hours
============================================================
```

---

### Agronomic Operations CLI

```bash
# Run diagnostics on sample field surveys
python diagnose.py --demo

# Validate agronomy stoichiometry unit tests
pytest tests/ -v
```

Field data contracts, FAO-56 irrigation standards, and agronomic guidelines are detailed in [AGRONOMY_STANDARDS.md](AGRONOMY_STANDARDS.md).
