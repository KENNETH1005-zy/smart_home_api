from fastapi import FastAPI
from app.routers import users, houses, rooms, devices
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Home API", version="1.0")

# Register routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(houses.router, prefix="/houses", tags=["Houses"])
app.include_router(rooms.router, prefix="/rooms", tags=["Rooms"])
app.include_router(devices.router, prefix="/devices", tags=["Devices"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Home API"}