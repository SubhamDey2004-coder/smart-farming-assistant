from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.farmer_model import Farmer
from app.schemas.farmer_schema import (
    FarmerCreate,
    FarmerResponse
)

router = APIRouter(
    prefix="/farmers",
    tags=["Farmers"]
)


# GET ALL FARMERS
@router.get("/", response_model=list[FarmerResponse])
def get_all_farmers(db: Session = Depends(get_db)):
    farmers = db.query(Farmer).all()
    return farmers


# GET FARMER BY FARMER_ID
@router.get("/{farmer_id}", response_model=FarmerResponse)
def get_farmer(farmer_id: str, db: Session = Depends(get_db)):

    farmer = db.query(Farmer).filter(
        Farmer.farmer_id == farmer_id
    ).first()

    if not farmer:
        raise HTTPException(
            status_code=404,
            detail="Farmer not found"
        )

    return farmer


# CREATE FARMER
@router.post("/", response_model=FarmerResponse)
def create_farmer(
    farmer_data: FarmerCreate,
    db: Session = Depends(get_db)
):

    existing_farmer = db.query(Farmer).filter(
        Farmer.farmer_id == farmer_data.farmer_id
    ).first()

    if existing_farmer:
        raise HTTPException(
            status_code=400,
            detail="Farmer ID already exists"
        )

    new_farmer = Farmer(**farmer_data.model_dump())

    db.add(new_farmer)
    db.commit()
    db.refresh(new_farmer)

    return new_farmer


# UPDATE FARMER
@router.put("/{farmer_id}", response_model=FarmerResponse)
def update_farmer(
    farmer_id: str,
    updated_data: FarmerCreate,
    db: Session = Depends(get_db)
):

    farmer = db.query(Farmer).filter(
        Farmer.farmer_id == farmer_id
    ).first()

    if not farmer:
        raise HTTPException(
            status_code=404,
            detail="Farmer not found"
        )

    for key, value in updated_data.model_dump().items():
        setattr(farmer, key, value)

    db.commit()
    db.refresh(farmer)

    return farmer


# DELETE FARMER
@router.delete("/{farmer_id}")
def delete_farmer(
    farmer_id: str,
    db: Session = Depends(get_db)
):

    farmer = db.query(Farmer).filter(
        Farmer.farmer_id == farmer_id
    ).first()

    if not farmer:
        raise HTTPException(
            status_code=404,
            detail="Farmer not found"
        )

    db.delete(farmer)
    db.commit()

    return {
        "message": "Farmer deleted successfully"
    }