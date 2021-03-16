from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import database
from ..database import disease_crud
from ..schemas import disease_schemas

diseases_router = APIRouter(
    prefix="/diseases",
    tags=["diseases"],
)

crudObj = disease_crud.CRUD_disease()

# route to get all the disease 
@diseases_router.get("/")
def get_all_disease(id: int = -1, db: Session = Depends(database.get_db_session), limit: int = 10):
    print("on va faire la query")
    print("")
    all_disease = crudObj.get_all_disease(db, limit)
    return all_disease

@diseases_router.get("/type")
def get_all_disease(id: int = -1, db: Session = Depends(database.get_db_session), limit: int = 10):
    print("on va faire la query ppour les type")
    all_disease_type = crudObj.get_all_disease_type(db, limit)
    return all_disease_type

# note : je dirais que seul les admin pourrait en rajouter non ?
@diseases_router.post("/")
def add_a_disease(body_disease: disease_schemas.baseDisease, db: Session = Depends(database.get_db_session)):
    print("le body")
    print(body_disease)
    new_disease_added = crudObj.add_a_disease(db, body_disease)
    return new_disease_added


@diseases_router.put("/")
def put_disease(body_disease: disease_schemas.baseDisease, db: Session = Depends(database.get_db_session)):
    crudObj.update_disease(db, body_disease)
    return {"message":"in progress"}


@diseases_router.patch("/")
def patch_disease(body_disease: disease_schemas.baseDisease, db: Session = Depends(database.get_db_session)):
    
    crudObj.update_disease(db, body_disease)
    return {"message":"in pprogress"}


# on va vraiment faire un delete ? en tout cas seul les admins devrait pouvoir le faire non ?
@diseases_router.post("/")
def delete_a_disease(body: disease_schemas.baseDisease, db: Session = Depends(database.get_db_session)):

    return {"message":"in pprogress"}