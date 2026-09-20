# AgriShield — Autonomous Precision Crop Pathology & Soil Nutrient Balancer

[![OpenGAP Compliant](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](https://opengap.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Autonomous agricultural diagnostics agent for multispectral leaf pathology identification, soil nutrient deficit mitigation, and drought stress forecasting.

## Domain Category
**Other**

## Architecture
- **OpenGAP Specification**: `0.1.0`
- **Role**: Precision Agronomist and Crop Pathologist
- **Primary Goal**: Identify foliar fungal and bacterial pathogens from spectral imagery, calculate nitrogen-phosphorus-potassium remediation, and forecast soil moisture deficit curves.

## Skills Included
- **`foliar-pathology-screening`**: Extracting visual necrotic lesions and chlorosis patterns to distinguish Cercospora from Septoria and rust strains.
- **`npk-nutrient-balancing`**: Calculating stoichiometric soil amendment requirements based on cation exchange capacity (CEC) and target crop yield.
- **`evapotranspiration-forecasting`**: Modeling Penman-Monteith reference evapotranspiration to schedule deficit irrigation windows.

## Tools Schema
- **`analyze-spectral-imagery`**: Compute normalized difference vegetation index (NDVI) and red-edge chlorophyll index across field plots.
- **`calculate-soil-amendment`**: Generate fertilizer prescription per hectare based on soil test chemistry and crop uptake stage.
- **`model-drought-stress-index`**: Evaluate root zone soil water depletion fraction against field capacity.

## Explainability & Verification
Full explainability compliance under OpenGAP Checkpoint 2 is detailed in [EXPLAINABILITY.md](EXPLAINABILITY.md), covering:
- Decision Reasoning
- Data Sources and Inputs Used
- Confidence Scoring Methodology
- Source Attribution Protocol
- Bias Awareness
- Limitation Taxonomy per Domain
- Uncertainty Quantification Approach

## Multi-Framework Compatibility
Adapters and visa export configurations are included in `exports/`:
- Anthropic Claude (`claude-system-prompt.txt`)
- OpenAI Assistants (`openai-assistant.json`)
- LangChain (`langchain-agent.json`)
- CrewAI (`crewai-agent.json`)
- AutoGen (`autogen-agent.json`)

## License
MIT License
