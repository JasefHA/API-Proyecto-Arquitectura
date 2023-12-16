# main.py
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base  # Ruta correcta para importar Base desde models
from routes.routes import router  # Ruta correcta para importar el enrutador desde routes
from database import get_db

app = FastAPI()

# Agrega las rutas al enrutador principal
app.include_router(router)