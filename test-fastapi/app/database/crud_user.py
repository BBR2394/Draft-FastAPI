from sqlalchemy.orm import Session

from . import mdl

def get_all_user(dbSession: Session, skip: int = 0, limit: int = 100):
    return dbSession.query(mdl.User).offset(skip).limit(limit).all()

def get_all_user_all_data(dbSession: Session, skip: int = 0, limit: int = 100):
    return dbSession.query(mdl.UserAllInfo).offset(skip).limit(limit).all()

def get_one_user(dbSession: Session, idToFind: int):
    one_user = dbSession.query(mdl.User).filter(mdl.User.id == idToFind).first()
    return one_user

def get_one_user_all_data(dbSession: Session, idToFind: int):
    one_user = dbSession.query(mdl.UserAllInfo).filter(mdl.UserAllInfo.id == idToFind).first()
    return one_user

def put_a_user_mail(dbSession: Session, newMail: str, idToFind: int):
    user_to_up = dbSession.query(mdl.UserAllInfo).filter(mdl.UserAllInfo.id == idToFind).first()
    user_to_up.email = newMail
    dbSession.commit()
    user_updated = dbSession.query(mdl.UserAllInfo).filter(mdl.UserAllInfo.id == idToFind).first()
    return user_updated

def delete_a_user(dbSession: Session, idToFind: int):
    user_to_del = dbSession.query(mdl.User).filter(mdl.User.id == idToFind).first()
    dbSession.delete(user_to_del)
    dbSession.commit()
    return user_to_del