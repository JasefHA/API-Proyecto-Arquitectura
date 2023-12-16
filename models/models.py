# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()

class Area(Base):
    __tablename__ = "areas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    employees = relationship("Employee", back_populates="area")

class AreaModel(BaseModel):
    name: str
    

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    area_id = Column(Integer, ForeignKey("areas.id"))
    supervisor_id = Column(Integer, ForeignKey("supervisors.id"))
    schedule_id = Column(Integer, ForeignKey("schedules.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    area = relationship("Area", back_populates="employees")
    supervisor = relationship("Supervisor", back_populates="subordinates", foreign_keys=[supervisor_id])
    schedule = relationship("Schedule")

class EmployeeModel(BaseModel):
    name: str
    area_id: int
    supervisor_id: int
    schedule_id: int

class Supervisor(Base):
    __tablename__ = "supervisors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    subordinates = relationship("Employee", back_populates="supervisor", foreign_keys=[Employee.supervisor_id])

class SupervisorModel(BaseModel):
    name: str

class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class ScheduleModel(BaseModel):
    name: str
