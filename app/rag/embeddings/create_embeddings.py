import os
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

db = SessionLocal()

farmers = db.query(Farmer).all()

documents = []
farmer_ids = []

for farmer in farmers:

    text = f"""
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
    Previous Yield: {farmer.previous_yield_ton}
    Pest History: {farmer.pest_history}
    Current Season: {farmer.current_season}
    Rainfall Forecast: {farmer.rainfall_forecast_mm}
    Temperature: {farmer.temperature_c}
    Humidity: {farmer.humidity_percent}
    Market Demand: {farmer.market_demand}
    """

    documents.append(text)
    farmer_ids.append(farmer.farmer_id)


# Generate embeddings
embeddings = model.encode(documents)

embedding_dimension = embeddings.shape[1]

# Create FAISS index
index = faiss.IndexFlatL2(embedding_dimension)

index.add(np.array(embeddings))


# Save FAISS index
os.makedirs("app/rag/vector_store", exist_ok=True)

faiss.write_index(
    index,
    "app/rag/vector_store/farmer_index.faiss"
)

# Save farmer mapping
with open(
    "app/rag/vector_store/farmer_mapping.pkl",
    "wb"
) as f:

    pickle.dump(
        {
            "documents": documents,
            "farmer_ids": farmer_ids
        },
        f
    )

print("Embeddings and FAISS index created successfully.")

db.close()