import pickle

import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

from app.core.database import SessionLocal
from app.models.farmer_model import Farmer


# Load embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


# Load FAISS index
index = faiss.read_index(
    "app/rag/vector_store/farmer_index.faiss"
)


# Load mapping
with open(
    "app/rag/vector_store/farmer_mapping.pkl",
    "rb"
) as f:

    mapping = pickle.load(f)

documents = mapping["documents"]
farmer_ids = mapping["farmer_ids"]


def get_farmer_profile(farmer_id: str):

    db = SessionLocal()

    farmer = db.query(Farmer).filter(
        Farmer.farmer_id == farmer_id
    ).first()

    db.close()

    if not farmer:
        return None

    profile = f"""
    Farmer Name: {farmer.name}

    Region: {farmer.region}

    Soil Type: {farmer.soil_type}

    Soil pH: {farmer.soil_ph}

    Soil Moisture: {farmer.soil_moisture}

    Nitrogen Level: {farmer.nitrogen}

    Phosphorus Level: {farmer.phosphorus}

    Potassium Level: {farmer.potassium}

    Organic Carbon: {farmer.organic_carbon}

    Current Crop: {farmer.crop_type}

    Crop Stage: {farmer.crop_stage}

    Irrigation Type: {farmer.irrigation_type}

    Water Availability: {farmer.water_availability}

    Previous Crop: {farmer.previous_crop}

    Fertilizer Used: {farmer.fertilizer_used}

    Previous Yield: {farmer.previous_yield_ton} tons

    Pest History: {farmer.pest_history}

    Current Season: {farmer.current_season}

    Rainfall Forecast: {farmer.rainfall_forecast_mm} mm

    Temperature: {farmer.temperature_c} degree Celsius

    Humidity: {farmer.humidity_percent} percent

    Market Demand: {farmer.market_demand}
    """

    return profile


def retrieve_agriculture_context(
    query: str,
    top_k: int = 1
):

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        top_k
    )

    contexts = []

    for idx in indices[0]:
        contexts.append(documents[idx])

    return contexts

def get_farmer_object(farmer_id: str):

    db = SessionLocal()

    farmer = db.query(Farmer).filter(
        Farmer.farmer_id == farmer_id
    ).first()

    db.close()

    return farmer