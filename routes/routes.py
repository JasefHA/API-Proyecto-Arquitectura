# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.models import Area, AreaModel, Employee, EmployeeModel,Supervisor,SupervisorModel, Schedule, ScheduleModel
from database import get_db

router = APIRouter()

@router.get("/")
async def hello():
    return{"message":"Hola Mundo"}

@router.get("/areas/", response_model=list[AreaModel])
def get_all_areas(db: Session = Depends(get_db)):
    areas = db.query(Area).all()
    return areas

@router.get("/employees/", response_model=list[EmployeeModel])
def get_all_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees

@router.get("/schedules/", response_model=list[ScheduleModel])
def get_all_schedules(db: Session = Depends(get_db)):
    schedules = db.query(Schedule).all()
    return schedules

@router.get("/supervisors/", response_model=list[SupervisorModel])
def get_all_supervisors(db: Session = Depends(get_db)):
    supervisors = db.query(Supervisor).all()
    return supervisors

'''
@router.get("/supervisor_logs/", response_model=list[SupervisorLogModel])
def get_all_supervisor_logs(db: Session = Depends(get_db)):
    logs = db.query(SupervisorLog).all()
    return logs
'''

@router.post("/area/", response_model=AreaModel)
def create_area(area: AreaModel, db: Session = Depends(get_db)):
    db_area = Area(**area.dict())
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area

@router.post("/supervisors/", response_model=SupervisorModel)  # Agregado para crear supervisores
def create_supervisor(supervisor: SupervisorModel, db: Session = Depends(get_db)):
    new_supervisor = Supervisor(**supervisor.dict())
    db.add(new_supervisor)
    db.commit()
    db.refresh(new_supervisor)
    return new_supervisor

@router.post("/employees/", response_model=EmployeeModel)
def create_employee(employee: EmployeeModel, db: Session = Depends(get_db)):
    new_employee = Employee(**employee.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

@router.put("/areas/{area_name}")
def update_area(area_name: str, updated_area: AreaModel, db: Session = Depends(get_db)):
    area = db.query(Area).filter(Area.name == area_name).first()
    if area:
        area.name = updated_area.name
        db.commit()
        db.refresh(area)
        return area
    else:
        raise HTTPException(status_code=404, detail="Area not found")

@router.delete("/areas/{area_name}")
def delete_area(area_name: str, db: Session = Depends(get_db)):
    area = db.query(Area).filter(Area.name == area_name).first()
    if area:
        db.delete(area)
        db.commit()
        return {"message": "Area deleted"}
    else:
        raise HTTPException(status_code=404, detail="Area not found")

