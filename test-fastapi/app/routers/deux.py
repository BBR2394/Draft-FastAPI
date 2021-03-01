from fastapi import APIRouter

# j'ai nommé mon router : deux
routerDeux = APIRouter(
    prefix="/dd",
    tags=["dd"],
)


@routerDeux.get("/")
def testdeuxiemefichier():
    print("toto")
    return { "message": "salut" }


@routerDeux.get("/home")
def read_root():
    return {"Hello": "World"}