from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
    farmer_id: str
    query: str


class ChatResponse(BaseModel):
    farmer_id: str
    recommendations: List[str]
    reason: str