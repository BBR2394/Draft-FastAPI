from sqlalchemy.orm import Session

from . import horse_mdl
from . import schemas_hms

# def get_horses(db: Session, horse_id: int):
#    return db.query(model.horse_mdl.horse).filter()


def get_horses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(horse_mdl.horse).offset(skip).limit(limit).all()


def get_one_horses(db: Session, id: int):
    #return db.query(models.User).filter(models.User.id == user_id).first()
    return db.query(horse_mdl.horse).filter(horse_mdl.horse.horse_id == id).first()

def del_one_horse(db: Session, id: int):
    horse_to_delete = db.query(horse_mdl.horse).filter(horse_mdl.horse.horse_id == id).first()
    db.delete(horse_to_delete)
    db.commit()
    return horse_to_delete