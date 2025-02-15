from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Room, House
from app.database import get_db

router = APIRouter()

@router.post("/")
def create_room(name: str, house_id: int, db: Session = Depends(get_db)):
    house = db.query(House).filter(House.id == house_id).first()
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    room = Room(name=name, house_id=house_id)
    db.add(room)
    db.commit()
    return room

@router.get("/{room_id}")
def get_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room