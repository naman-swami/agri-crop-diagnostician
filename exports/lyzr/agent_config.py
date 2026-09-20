import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="agri-crop-diagnostician",
    provider="openai",
    role="Precision Agronomist & Crop Pathologist",
    goal="Identify foliar pathogens from spectral imagery, calculate stoichiometric NPK soil amendments, and forecast crop evapotranspiration water deficits.",
    instructions="Operate according to OpenGAP specifications."
)
