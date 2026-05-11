from app.core.database import engine
from app.models.farmer_model import Base

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")