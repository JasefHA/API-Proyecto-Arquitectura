# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.models import Area, AreaModel, Employee, EmployeeModel, SupervisorLog, Schedule, ScheduleModel
from database import get_db

router = APIRouter()

@router.get("/")
async def hello():
    return{"message":"Hola Mundo"}

@router.get("/areas/", response_model=list[AreaModel])
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

