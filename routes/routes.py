# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.models import Area, AreaModel, Employee, EmployeeModel, Supervisor, SupervisorModel, Schedule, ScheduleModel
from database import get_db

router = APIRouter()

@router.get("/")
async def hello():
    return {"message": "Bienvenido a la mejor API"}

# CRUD operations for Area
@router.get("/areas/", response_model=list[AreaModel])
def get_all_areas(db: Session = Depends(get_db)):
    areas = db.query(Area).all()
    return areas

@router.get("/areas/{area_id}", response_model=AreaModel)
def get_area_by_id(area_id: int, db: Session = Depends(get_db)):
    area = db.query(Area).filter(Area.id == area_id).first()
    if area:
        return area
    else:
        raise HTTPException(status_code=404, detail="Area not found")

@router.get("/areas/name/{area_name}", response_model=AreaModel)
def get_area_by_name(area_name: str, db: Session = Depends(get_db)):
    area = db.query(Area).filter(Area.name == area_name).first()
    if area:
        return area
    else:
        raise HTTPException(status_code=404, detail="Area not found")

@router.post("/areas/", response_model=AreaModel)
def create_area(area: AreaModel, db: Session = Depends(get_db)):
    db_area = Area(**area.dict())
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area

@router.put("/areas/{area_id}")
def update_area(area_id: int, updated_area: AreaModel, db: Session = Depends(get_db)):
    area = db.query(Area).filter(Area.id == area_id).first()
    if area:
        area.name = updated_area.name
        db.commit()
        db.refresh(area)
        return area
    else:
        raise HTTPException(status_code=404, detail="Area not found")

@router.delete("/areas/{area_id}")
def delete_area(area_id: int, db: Session = Depends(get_db)):
    area = db.query(Area).filter(Area.id == area_id).first()
    if area:
        db.delete(area)
        db.commit()
        return {"message": "Area deleted"}
    else:
        raise HTTPException(status_code=404, detail="Area not found")

# CRUD operations for Employee
@router.get("/employees/", response_model=list[EmployeeModel])
def get_all_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees

@router.get("/employees/{employee_id}", response_model=EmployeeModel)
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        return employee
    else:
        raise HTTPException(status_code=404, detail="Employee not found")

@router.get("/employees/name/{employee_name}", response_model=EmployeeModel)
def get_employee_by_name(employee_name: str, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.name == employee_name).first()
    if employee:
        return employee
    else:
        raise HTTPException(status_code=404, detail="Employee not found")

@router.post("/employees/", response_model=EmployeeModel)
def create_employee(employee: EmployeeModel, db: Session = Depends(get_db)):
    new_employee = Employee(**employee.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

@router.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: EmployeeModel, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        employee.name = updated_employee.name
        employee.area_id = updated_employee.area_id
        employee.supervisor_id = updated_employee.supervisor_id
        employee.schedule_id = updated_employee.schedule_id
        db.commit()
        db.refresh(employee)
        return employee
    else:
        raise HTTPException(status_code=404, detail="Employee not found")

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
        return {"message": "Employee deleted"}
    else:
        raise HTTPException(status_code=404, detail="Employee not found")


## CRUD operations for Schedule
@router.get("/schedules/", response_model=list[ScheduleModel])
def get_all_schedules(db: Session = Depends(get_db)):
    schedules = db.query(Schedule).all()
    return schedules

@router.get("/schedules/{schedule_id}", response_model=ScheduleModel)
def get_schedule_by_id(schedule_id: int, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if schedule:
        return schedule
    else:
        raise HTTPException(status_code=404, detail="Schedule not found")

@router.get("/schedules/name/{schedule_name}", response_model=ScheduleModel)
def get_schedule_by_name(schedule_name: str, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.name == schedule_name).first()
    if schedule:
        return schedule
    else:
        raise HTTPException(status_code=404, detail="Schedule not found")

@router.post("/schedules/", response_model=ScheduleModel)
def create_schedule(schedule: ScheduleModel, db: Session = Depends(get_db)):
    new_schedule = Schedule(**schedule.dict())
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    return new_schedule

@router.put("/schedules/{schedule_id}")
def update_schedule(schedule_id: int, updated_schedule: ScheduleModel, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if schedule:
        schedule.name = updated_schedule.name
        db.commit()
        db.refresh(schedule)
        return schedule
    else:
        raise HTTPException(status_code=404, detail="Schedule not found")

@router.delete("/schedules/{schedule_id}")
def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if schedule:
        db.delete(schedule)
        db.commit()
        return {"message": "Schedule deleted"}
    else:
        raise HTTPException(status_code=404, detail="Schedule not found")


# CRUD operations for Supervisor
@router.get("/supervisors/", response_model=list[SupervisorModel])
def get_all_supervisors(db: Session = Depends(get_db)):
    supervisors = db.query(Supervisor).all()
    return supervisors

@router.get("/supervisors/{supervisor_id}", response_model=SupervisorModel)
def get_supervisor_by_id(supervisor_id: int, db: Session = Depends(get_db)):
    supervisor = db.query(Supervisor).filter(Supervisor.id == supervisor_id).first()
    if supervisor:
        return supervisor
    else:
        raise HTTPException(status_code=404, detail="Supervisor not found")

@router.get("/supervisors/name/{supervisor_name}", response_model=SupervisorModel)
def get_supervisor_by_name(supervisor_name: str, db: Session = Depends(get_db)):
    supervisor = db.query(Supervisor).filter(Supervisor.name == supervisor_name).first()
    if supervisor:
        return supervisor
    else:
        raise HTTPException(status_code=404, detail="Supervisor not found")

@router.post("/supervisors/", response_model=SupervisorModel)
def create_supervisor(supervisor: SupervisorModel, db: Session = Depends(get_db)):
    new_supervisor = Supervisor(**supervisor.dict())
    db.add(new_supervisor)
    db.commit()
    db.refresh(new_supervisor)
    return new_supervisor

@router.put("/supervisors/{supervisor_id}")
def update_supervisor(supervisor_id: int, updated_supervisor: SupervisorModel, db: Session = Depends(get_db)):
    supervisor = db.query(Supervisor).filter(Supervisor.id == supervisor_id).first()
    if supervisor:
        supervisor.name = updated_supervisor.name
        db.commit()
        db.refresh(supervisor)
        return supervisor
    else:
        raise HTTPException(status_code=404, detail="Supervisor not found")

@router.delete("/supervisors/{supervisor_id}")
def delete_supervisor(supervisor_id: int, db: Session = Depends(get_db)):
    supervisor = db.query(Supervisor).filter(Supervisor.id == supervisor_id).first()
    if supervisor:
        db.delete(supervisor)
        db.commit()
        return {"message": "Supervisor deleted"}
    else:
        raise HTTPException(status_code=404, detail="Supervisor not found")

