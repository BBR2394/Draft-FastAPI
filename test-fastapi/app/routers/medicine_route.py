from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import crud_med, crud_generic, database
from ..schemas import Med_schms
from ..database.model import medicine_model

# j'ai nommé mon router : deux
med_route = APIRouter(
    prefix="/medicine",
    tags=["medicine"],
)


@med_route.get("/")
def getAllMedicine(id: int = -1, db: Session = Depends(database.get_db_session)):
    all_med = crud_generic.get_all_data(db, medicine_model.medicament)
    return all_med
    #return {"message": "in progress"}

@med_route.post("/")
def addMedoc(bodyMed: Med_schms.med):
    print("je vais rajouter : ")
    print(bodyMed)
    return {"message": "in progress"}

@med_route.get("/more")
def getAllMedicineMore(id: int = -1, db: Session = Depends(database.get_db_session)):
    all_med_more = crud_generic.get_all_data(db, medicine_model.medicament_with_type)
    return all_med_more