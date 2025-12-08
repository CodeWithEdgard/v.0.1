from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.domains.usuarios.models import Usuario

router = APIRouter()

dados = {
    "id": 1,
    "nome": "edgar",
    "sobrenome": "mendes",
}


@router.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):

    return db.query(Usuario).all()
