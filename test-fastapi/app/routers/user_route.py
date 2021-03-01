from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from typing import Optional
from pydantic import BaseModel

from ..database import database, crud_user

# j'ai nommé mon router : deux
route_user = APIRouter(
    prefix="/user",
    tags=["user"],
)

# c'est ceci le schema
class userBody(BaseModel):
    id: Optional[int]
    # attention met des chaine vide quand rien n'est donné
    email: Optional[str] = None
    last_name: Optional[str]
    first_name: Optional[str]
    username: Optional[str]
    moreInfo: bool

# it is calle by function Depend from fast api
def get_db_session():
    db = database.dbSessionLocal()
    try:
        yield db
    finally:
        db.close()

@route_user.get("/test")
def testdeuxiemefichier():
    print("we are going to get data from bdd")
    return {"message": "user"}


@route_user.get("/")
def get_al_users(id: int = -1, alldata: int=0, db: Session = Depends(get_db_session)):
    if id == -1:
        if alldata == 0:
            all_usr = crud_user.get_all_user(db)
        else:
            all_usr = crud_user.get_all_user_all_data(db)
    else:
        if alldata  == 0:
            all_usr = crud_user.get_one_user_all_data(db, id)
        else:
            all_usr = crud_user.get_one_user(db, id)
    return all_usr

#@route_user.get()
#def get_al_users():
#    return {"message": "GET one user"}


@route_user.post("/")
def get_one_users(bdy: userBody, db: Session = Depends(get_db_session)):
    if bdy.moreInfo:
        one_usr = crud_user.get_one_user_all_data(db, bdy.id)
    else:
        one_usr = crud_user.get_one_user(db, bdy.id)
    return one_usr



@route_user.put("/")
def put_one_user(bdy: userBody, db: Session = Depends(get_db_session)):
    print(bdy)
    print(bdy.id)
    user_updated = crud_user.put_a_user_mail(db, bdy.email, bdy.id)
    #return {"message": "PUT one user"}
    return user_updated


@route_user.delete("/")
def delete_one_user(bdy: userBody, db: Session = Depends(get_db_session)):
    usr_to_del = crud_user.delete_a_user(db, bdy.id)

    return usr_to_del

#@route_user.("/")