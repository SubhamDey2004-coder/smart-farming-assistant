from pydantic import BaseModel
from typing import Optional


class FarmerBase(BaseModel):
    farmer_id: str
    name: str
    region: str

    soil_type: str
    soil_ph: float
    soil_moisture: float

    nitrogen: float
    phosphorus: float
    potassium: float

    organic_carbon: float

    crop_type: str
    crop_stage: str

    irrigation_type: str
    water_availability: str

    previous_crop: str
    fertilizer_used: str

    previous_yield_ton: float

    pest_history: Optional[str] = None

    current_season: str

    rainfall_forecast_mm: float

    temperature_c: float

    humidity_percent: float

    market_demand: str


class FarmerCreate(FarmerBase):
    pass


class FarmerResponse(FarmerBase):
    id: int

    class Config:
        from_attributes = True