# main.py
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base  # Ruta correcta para importar Base desde models
from routes.routes import router  # Ruta correcta para importar el enrutador desde routes
from database import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # Agrega la URL de tu aplicación React
    "https://main.d37yeuc6iylap9.amplifyapp.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agrega las rutas al enrutador principal
app.include_router(router)