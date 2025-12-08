from fastapi import FastAPI
from app.domains.usuarios.routes import router as usuarios_router


app = FastAPI()


@app.get("/")
def init():
    return {"msg": "voce conseguiu"}


app.include_router(usuarios_router, tags=["Usuarios"])
