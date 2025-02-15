from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import House, User
from app.database import get_db
import jwt
import os

router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
ALGORITHM = "HS256"

def get_current_user(token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/")
def create_house(name: str, token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)
    house = House(name=name, owner_id=user.id)
    db.add(house)
    db.commit()
    return house

@router.get("/{house_id}")
def get_house(house_id: int, db: Session = Depends(get_db)):
    house = db.query(House).filter(House.id == house_id).first()
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    return house