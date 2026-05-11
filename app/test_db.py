from app.core.database import SessionLocal
from app.models.farmer_model import Farmer

db = SessionLocal()

farmers = db.query(Farmer).all()

for farmer in farmers:
    print(farmer.name, farmer.crop_type)

db.close()