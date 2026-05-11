from app.core.database import SessionLocal
from app.models.farmer_model import Farmer


db = SessionLocal()

farmers = db.query(Farmer).all()

documents = []

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

    Previous Yield: {farmer.previous_yield_ton} tons

    Pest History: {farmer.pest_history}

    Current Season: {farmer.current_season}

    Rainfall Forecast: {farmer.rainfall_forecast_mm} mm

    Temperature: {farmer.temperature_c} degree Celsius

    Humidity: {farmer.humidity_percent} percent

    Market Demand: {farmer.market_demand}
    """

    documents.append({
        "farmer_id": farmer.farmer_id,
        "content": text
    })


for doc in documents:
    print(doc["content"])
    print("=" * 80)

db.close()