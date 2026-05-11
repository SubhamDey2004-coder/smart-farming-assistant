from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base


class Farmer(Base):
    __tablename__ = "farmers"

    id = Column(Integer, primary_key=True, index=True)

    farmer_id = Column(String, unique=True, nullable=False)
    name = Column(String)
    region = Column(String)

    soil_type = Column(String)
    soil_ph = Column(Float)
    soil_moisture = Column(Float)

    nitrogen = Column(Float)
    phosphorus = Column(Float)
    potassium = Column(Float)

    organic_carbon = Column(Float)

    crop_type = Column(String)
    crop_stage = Column(String)

    irrigation_type = Column(String)
    water_availability = Column(String)

    previous_crop = Column(String)
    fertilizer_used = Column(String)

    previous_yield_ton = Column(Float)

    pest_history = Column(String)

    current_season = Column(String)

    rainfall_forecast_mm = Column(Float)

    temperature_c = Column(Float)

    humidity_percent = Column(Float)

    market_demand = Column(String)