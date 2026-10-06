import os
import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from app.core.database import SessionLocal
from app.models.farmer_model import Farmer


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
INDEX_PATH = os.path.join(
    BASE_DIR, "rag", "vector_store", "farmer_index.faiss"
)
MAPPING_PATH = os.path.join(
    BASE_DIR, "rag", "vector_store", "farmer_mapping.pkl"
)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def _load_vector_store():
    if not os.path.exists(INDEX_PATH) or not os.path.exists(MAPPING_PATH):
        return None, []

    index = faiss.read_index(INDEX_PATH)

    with open(MAPPING_PATH, "rb") as file:
        mapping = pickle.load(file)

    return index, mapping.get("documents", [])


def get_farmer_profile(farmer_id: str):
    db = SessionLocal()

    try:
        farmer = (
            db.query(Farmer)
            .filter(Farmer.farmer_id == farmer_id)
            .first()
        )

        if not farmer:
            return None

        return f"""
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
""".strip()
    finally:
        db.close()


def retrieve_agriculture_context(query: str, top_k: int = 1):
    index, documents = _load_vector_store()

    if index is None or not documents:
        return []

    query_embedding = model.encode([query])
    top_k = min(top_k, len(documents))

    _, indices = index.search(
        np.asarray(query_embedding, dtype="float32"),
        top_k,
    )

    return [
        documents[idx]
        for idx in indices[0]
        if idx != -1 and idx < len(documents)
    ]


def get_farmer_object(farmer_id: str):
    db = SessionLocal()

    try:
        return (
            db.query(Farmer)
            .filter(Farmer.farmer_id == farmer_id)
            .first()
        )
    finally:
        db.close()
