# Precision Agronomy Standards & Soil Stoichiometry

## 1. Multispectral Vegetation Indices & Remote Sensing
Agri Crop Diagnostician processes Sentinel-2 MSI (MultiSpectral Instrument) surface reflectance data calibrated under **FAO-56 Irrigation and Drainage Guidelines**:

### A. Normalized Difference Vegetation Index (NDVI)
$$NDVI = \frac{\rho_{\text{NIR}} - \rho_{\text{RED}}}{\rho_{\text{NIR}} + \rho_{\text{RED}}}$$
- **Band 8 (NIR, 842 nm)** vs. **Band 4 (Red, 665 nm)**.
- *Calibration Scale*:
  - $< 0.10$: Bare soil, rock, or standing water.
  - $0.20 - 0.40$: Sparse or severely stressed vegetation / severe chlorosis.
  - $0.40 - 0.65$: Moderate canopy development; typical vegetative stage.
  - $> 0.65$: Dense, healthy, vigorous crop canopy with high biomass.

### B. Normalized Difference Water Index (NDWI)
$$NDWI = \frac{\rho_{\text{NIR}} - \rho_{\text{SWIR}}}{\rho_{\text{NIR}} + \rho_{\text{SWIR}}}$$
- **Band 8 (NIR, 842 nm)** vs. **Band 11 (SWIR, 1610 nm)**.
- Gauges liquid water content in the plant canopy. Values $< 0.20$ indicate significant leaf dehydration requiring immediate irrigation scheduling.

---

## 2. Soil Stoichiometric Amendment Formulations
The nutrient reconciliation engine balances measured topsoil (0–30 cm) available Nitrogen, Phosphorus, and Potassium against crop-specific uptake curves for *Zea mays* (Maize), *Triticum aestivum* (Wheat), and *Glycine max* (Soybean).

### A. Fertilizer Carrier Specifications
1. **Urea ($46-0-0$)**: $46\%$ elemental Nitrogen ($N$).
   $$\text{Prescribed Urea (kg/ha)} = \frac{\text{Target } N - \text{Soil } N}{0.46 \times \eta_N}$$
   Where $\eta_N \approx 0.65$ represents typical nitrogen use efficiency accounting for volatilization and leaching.
2. **Diammonium Phosphate / DAP ($18-46-0$)**: $18\% N$ and $46\% P_2O_5$.
   $$\text{Prescribed DAP (kg/ha)} = \frac{\text{Target } P_2O_5 - \text{Soil } P_2O_5}{0.46 \times \eta_P}$$
3. **Muriate of Potash / MOP ($0-0-60$)**: $60\% K_2O$.
   $$\text{Prescribed MOP (kg/ha)} = \frac{\text{Target } K_2O - \text{Soil } K_2O}{0.60 \times \eta_K}$$

---

## 3. Environmental Runoff & Buffer Zone Regulations
All fertilizer prescriptions comply with the **EU Nitrates Directive (91/676/EEC)** and **USDA Natural Resources Conservation Service (NRCS) Code 590**:
- No synthetic nitrogen application within 10 meters of surface watercourses.
- Split-dose application mandatory when total $N$ requirement exceeds $120\text{ kg/ha}$ to prevent groundwater nitrate contamination.
