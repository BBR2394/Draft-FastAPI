from typing import Optional
# le package qui gere l'api : Fast API
from fastapi import FastAPI, Depends

from pydantic import BaseModel

# ll
from .routers import deux, bddrouter, user_route
from .database import horse_mdl
from .database import database
from .database import crud

horse_mdl.dbBaseClass.metadata.create_all(bind=database.dbEngine)

app = FastAPI()

app.include_router(deux.routerDeux)
app.include_router(bddrouter.routerBDD)
app.include_router(user_route.route_user)


class horseBody(BaseModel):
    name: Optional[str]
    id: Optional[int]


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# Dependency
def get_db():
    db = database.dbSessionLocal()
    try:
        yield db
    finally:
        db.close()

lstItem = []


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/homeinfo')
def homeRoute():
    return '<h1>home page</h1><p>this is juste the home route for our api</p>'

@app.get("/horses")
def get_all_horses(db: database.dbSessionLocal = Depends(get_db)):
    horses = crud.get_horses(db)
    print(horses)
    for i in horses:
        print(i)
    return horses


def test(name: str):
    return "bonjour II"


@app.post("/horses")
def get_one_horse_with_id(bdy: horseBody, db: database.dbSessionLocal = Depends(get_db)):
    print(bdy)
    print(bdy.id)
    horses = crud.get_one_horses(db, bdy.id)
    return horses

@app.post("/newhorse")
def add_new_horse(bdy: horseBody, db: database.dbSessionLocal = Depends(get_db)):
    print(bdy)
    print(bdy.name)
    new_horse = crud.add_new_horse(db, bdy.name)
    return new_horse

@app.put("/horse")
def update_horse(bdy: horseBody, db: database.dbSessionLocal = Depends(get_db)):
    print(bdy)
    print(bdy.id)
    horse_updated = crud.get_one_horse_moreData(db, bdy.id)
    return horse_updated


@app.delete("/horse")
def delete_one_horse(bdy: horseBody, db: database.dbSessionLocal = Depends(get_db)):
    print(bdy)
    print(bdy.id)
    horse_deleted = crud.del_one_horse(db, bdy.id)
    return horse_deleted


@app.get("/print")
def printItem():
    for i in lstItem:
        print(i)
    return {"message": "ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/test")
def testput():
    return {"message": "test put"}

@app.delete("/test")
def testDelete():

    return {"message": "test delete"}