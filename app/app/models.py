from sqlalchemy import Column, Integer, String, Float, Date, JSON
from app.database import Base

class Meter(Base):
    __tablename__ = "meters"
    id = Column(String, primary_key=True)
    last_readings = Column(JSON)
    last_date = Column(Date)

class Bill(Base):
    __tablename__ = "bills"
    id = Column(Integer, primary_key=True, index=True)
    meter_id = Column(String)
    date = Column(Date)
    amount = Column(Float)
    details = Column(JSON)
