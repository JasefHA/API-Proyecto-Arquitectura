# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

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
    supervisor_id = Column(Integer, ForeignKey("employees.id"))
    schedule_id = Column(Integer, ForeignKey("schedules.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    area = relationship("Area", back_populates="employees")
    supervisor = relationship("Employee", remote_side=[id], back_populates="subordinates", uselist=False)
    subordinates = relationship("Employee", back_populates="supervisor")
    schedule = relationship("Schedule")
    supervisor_logs = relationship("SupervisorLog", back_populates="employee")

class EmployeeModel(BaseModel):
    name: str
    area_id: int
    supervisor_id: int
    schedule_id: int

class SupervisorLog(Base):
    __tablename__ = "supervisor_logs"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)

    employee = relationship("Employee", back_populates="supervisor_logs")

class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class ScheduleModel(BaseModel):
    name: str
