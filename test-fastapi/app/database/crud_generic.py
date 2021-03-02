from sqlalchemy.orm import Session
from typing import Generic


def get_all_data(dbSession: Session, mdl: Generic, skip: int = 0, limit: int = 100):
    return dbSession.query(mdl).offset(skip).limit(limit).all()
