from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, Session, class_mapper
from datetime import datetime
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

# Configura la URL de conexión a tu base de datos MySQL en AWS
DATABASE_URL = "mysql+mysqlconnector://admin:userpasssql21*@database-evidencia4.cqia1zfpzc2w.us-east-1.rds.amazonaws.com:3306/RecursosHumanos"
engine = create_engine(DATABASE_URL)

# Modelos SQLAlchemy
Base = declarative_base()

class Area(Base):
    __tablename__ = "areas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

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
    supervisor = relationship("Employee", remote_side=[id], back_populates="subordinates")
    subordinates = relationship("Employee", back_populates="supervisor")
    schedule = relationship("Schedule")

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

    # Asegúrate de agregar esta línea para establecer la relación en la dirección correcta
    employee = relationship("Employee", back_populates="supervisor_logs")


class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class ScheduleModel(BaseModel):
    name: str


Area.employees = relationship("Employee", back_populates="area")
Employee.supervisor_logs = relationship("SupervisorLog", back_populates="employee")
Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

# Rutas
'''
@app.post("/areas/", response_model=AreaResponse)
def create_area(area: Area, db: Session = Depends(get_db)):
    db_area = Area(**area.dict())
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return AreaResponse(id=db_area.id, name=db_area.name)


@app.get("/areas/", response_model=List[AreaResponse])
def get_all_areas(db: Session = Depends(get_db)):
    areas = db.query(Area).all()
    return [AreaResponse(**area.__dict__) for area in areas]

@app.get("/areas/{area_id}", response_model=AreaResponse)
def get_area_by_id(area_id: int, db: Session = Depends(get_db)):
    area = db.query(Area).filter(Area.id == area_id).first()
    if area:
        return AreaResponse(**area.__dict__)
    else:
        raise HTTPException(status_code=404, detail="Area not found")
'''

@app.get("/")
async def hello():
    return{"message":"Hola Mundo"}


@app.get("/areas/", response_model=List[AreaModel])
def get_all_areas(db: Session = Depends(get_db)):
    areas = db.query(Area).all()
    return areas
'''
@app.post("/employees/", response_model=EmployeeModel)
def create_employee(employee: EmployeeModel, db: Session = Depends(get_db)):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.post("/area/", response_model=AreaModel)
def create_area(area: AreaModel, db: Session = Depends(get_db)):
    db_area = Area(**area.dict())
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area

@app.post("/schedule/", response_model=ScheduleModel)
def create_area(schedule: ScheduleModel, db: Session = Depends(get_db)):
    db_schedule = Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

@app.put("/employees/{employee_id}")
def update_supervisor(employee_id: int, supervisor_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        employee.supervisor_id = supervisor_id
        db.commit()
        db.refresh(employee)
        return employee
    else:
        raise HTTPException(status_code=404, detail="Employee not found")
'''
'''
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''