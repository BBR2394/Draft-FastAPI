from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from ..database import database, crud_generic

from ..schemas import Med_schms

route_med = APIRouter(
    prefix="/med",
    tags=["med"]
)

@route_med.get("/")
def get_all_medicine(id: int = -1, db: Session = Depends(get_db_session))