# Explainability — agri-crop-diagnostician

## Decision Reasoning
AgriShield correlates red-edge reflectance indices with canopy temperature differentials, isolating fungal spore distribution patterns from uniform soil nutrient deficiencies.

## Data Sources and Inputs Used
Sentinel-2 multispectral satellite imagery, farm IoT soil moisture sensors, weather telemetry, and university agricultural extension guidelines.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, agri-crop-diagnostician assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, agri-crop-diagnostician will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, agri-crop-diagnostician explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
agri-crop-diagnostician actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Weather Force Majeure: Cannot prevent extreme hail damage or flash flooding.
- Biological Mutations: Cannot guarantee efficacy against unclassified novel pathogen strains.
- Chemical Application: Does not operate spray tractors or autonomously dispense regulated agrochemicals.
- Soil Physics: Cannot alter fundamental geological soil texture (e.g. converting clay to loam).

## Uncertainty Quantification Approach
When satellite imagery has high cloud cover, AgriShield lowers confidence scores below 0.80 and flags the plot for physical drone scouting.
