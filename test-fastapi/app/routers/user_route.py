from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from typing import Optional
from pydantic import BaseModel


from ..database import database, crud_user, crud_generic
from ..database import mdl

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
    group_name: Optional[str]
    items: Optional[str]
    moreInfo: bool
    nomdugroupe: Optional[str]

class group(BaseModel):
    id: Optional[int]
    type: Optional[str]

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
    print(all_usr[0].email)
    print(all_usr[0].usr)
    return all_usr

@route_user.get("/group")
def get_all_ugrp(id: int = -1, alldata: int=0, db: Session = Depends(get_db_session)):
    all_grp = crud_user.get_all_group(db)
    return all_grp

@route_user.get("/generic")
def get_al_users(id: int = -1, alldata: int=0, db: Session = Depends(get_db_session)):
    all_usr = crud_generic.get_all_data(db, mdl.User)
    return all_usr

@route_user.get("/doc")
def return_file_html():
    index = "app/views/index.html"
    return FileResponse(index)

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