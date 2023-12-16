from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def hello():
    return {"message":"hola mundo"}
#prueba