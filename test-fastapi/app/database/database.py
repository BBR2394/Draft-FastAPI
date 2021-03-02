# this is the bdd engine for the app

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://Baptiste:bonjour2394@127.0.0.1/AMP"

dbEngine = create_engine(SQLALCHEMY_DATABASE_URL)

dbSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=dbEngine)


# a base class that our class wil derivate
dbBaseClass = declarative_base()

dbBaseClass.metadata.create_all(bind=dbEngine)


def get_db():
    db = dbSessionLocal()
    try:
        yield db
    finally:
        db.close()


# it is calle by function Depend from fast api
def get_db_session():
    db = database.dbSessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    print("bonjour")