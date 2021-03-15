from sqlalchemy.orm import Session

from .model import horse_mdl
from ..schemas import schemas_hms

# def get_horses(db: Session, horse_id: int):
#    return db.query(model.horse_mdl.horse).filter()


def get_horses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(horse_mdl.horse).offset(skip).limit(limit).all()


def get_one_horses(db: Session, id: int):
    #return db.query(models.User).filter(models.User.id == user_id).first()
    return db.query(horse_mdl.horse).filter(horse_mdl.horse.horse_id == id).first()

def add_new_horse(db: Session, newHorseName: str):
    new_horse = horse_mdl.horse(horse_name=newHorseName)
    db.add(new_horse)
    db.commit()
    db.refresh(new_horse)
    return new_horse

# ma focntion put qui est mal nommée
def get_one_horse_moreData(db: Session, id: int):
    horse_to_up = db.query(horse_mdl.horseFull).filter(horse_mdl.horse.horse_id == id).first()
    #print(horse_to_up.__getitem__("current_owner"))
    print(horse_to_up)
    horse_to_up.horse_name = "Foo bar"
    print(horse_to_up)
    db.commit()
    horse_updated = db.query(horse_mdl.horseFull).filter(horse_mdl.horse.horse_id == id).first()
    return horse_updated


def del_one_horse(db: Session, id: int):
    horse_to_delete = db.query(horse_mdl.horse).filter(horse_mdl.horse.horse_id == id).first()
    db.delete(horse_to_delete)
    db.commit()
    return horse_to_delete