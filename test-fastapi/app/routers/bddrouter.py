from fastapi import APIRouter

#j'ai nommé mon router : deux
routerBDD = APIRouter(
    prefix="/bdd",
    tags=["bdd"],
)

@routerBDD.get("/")
def testdeuxiemefichier():
    print("we are going to get data from bdd")
    return { "message": "bdd" }

