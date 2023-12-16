from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://admin:userpasssql21*@database-evidencia4.cqia1zfpzc2w.us-east-1.rds.amazonaws.com:3306/RecursosHumanos"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()