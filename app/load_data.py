import pandas as pd

from app.core.database import SessionLocal
from app.models.farmer_model import Farmer


db = SessionLocal()

df = pd.read_csv("app/data/farmers.csv")

for _, row in df.iterrows():

    existing_farmer = db.query(Farmer).filter(
        Farmer.farmer_id == row["farmer_id"]
    ).first()

    if existing_farmer:
        continue

    farmer = Farmer(
        farmer_id=row["farmer_id"],
        name=row["name"],
        region=row["region"],
        soil_type=row["soil_type"],
        soil_ph=row["soil_ph"],
        soil_moisture=row["soil_moisture"],
        nitrogen=row["nitrogen"],
        phosphorus=row["phosphorus"],
        potassium=row["potassium"],
        organic_carbon=row["organic_carbon"],
        crop_type=row["crop_type"],
        crop_stage=row["crop_stage"],
        irrigation_type=row["irrigation_type"],
        water_availability=row["water_availability"],
        previous_crop=row["previous_crop"],
        fertilizer_used=row["fertilizer_used"],
        previous_yield_ton=row["previous_yield_ton"],
        pest_history=row["pest_history"],
        current_season=row["current_season"],
        rainfall_forecast_mm=row["rainfall_forecast_mm"],
        temperature_c=row["temperature_c"],
        humidity_percent=row["humidity_percent"],
        market_demand=row["market_demand"]
    )

    db.add(farmer)

db.commit()

db.close()

print("Farmers data inserted successfully.")