from fastapi import FastAPI

from app.api.routes.farmer_routes import (
    router as farmer_router
)

from app.api.routes.chat_routes import (
    router as chat_router
)

app = FastAPI(
    title="Smart Farming Assistant",
    version="1.0.0"
)

app.include_router(farmer_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "AI Smart Farming Assistant Backend Running"
    }