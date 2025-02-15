from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Device, Room
from app.database import get_db

router = APIRouter()

@router.post("/")
def create_device(type: str, room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    device = Device(type=type, room_id=room_id)
    db.add(device)
    db.commit()
    return device

@router.get("/{device_id}")
def get_device(device_id: int, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device