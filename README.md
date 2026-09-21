# AgriCrop Precision Foliar Diagnostician

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![AgriTech](https://img.shields.io/badge/Domain-Precision_Agriculture_Remote_Sensing-darkgreen.svg)](docs/fao56_evapotranspiration.md)
[![Standard](https://img.shields.io/badge/Model-FAO--56_Agronomy-green.svg)](docs/fao56_evapotranspiration.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

A precision agricultural remote sensing and foliar diagnostics platform calculating multispectral NDVI/NDWI canopy health indices and stoichiometric NPK fertilizer prescriptions.

```
                    ┌─────────────────────────┐
                    │ Multispectral Reflectance│
                    │   (NIR, RED, SWIR)      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ indices/spectral_indices│
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  NDVI Canopy Health │         │  NDWI Water Stress  │
      │ (Vigorous / Sparse) │         │ (Hydration Deficit) │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Prescription Blend Plan │
                    │ (Urea, DAP, MOP kg/ha)  │
                    └─────────────────────────┘
```

## Features

- **Multispectral Canopy Analysis**: Calculates precision NDVI and NDWI indices to evaluate foliar health and hydration stress.
- **Stoichiometric Fertilizer Optimization**: Prescribes exact Urea, DAP, and MOP kilograms per hectare required for target yields.
- **Agricultural Field Fixtures**: Pre-packaged with multispectral drone sensor survey datasets.

## Directory Structure

```
agri-crop-diagnostician/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint agronomic provenance
├── indices/
│   └── spectral_indices.py          # NDVI & NDWI spectral calculator
├── agronomy/
│   └── fertilizer_stoichiometry.py  # NPK nutrient balance engine
├── fixtures/
│   └── field_surveys/
│       └── sample_field_data.json   # Benchmark drone survey data
├── docs/
│   └── fao56_evapotranspiration.md  # Agronomic standards reference
├── tests/
│   └── test_agent.py                # Agronomic test suite
├── diagnose.py                          # Precision agriculture CLI
└── requirements.txt
```

## Quick Start

```bash
# Run agronomic test suite
pytest tests/ -v

# Audit sample field survey
python diagnose.py --demo
```
