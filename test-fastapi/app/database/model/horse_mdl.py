from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from ..database import dbBaseClass, dbEngine, dbBaseClass


class horse(dbBaseClass):
    __tablename__ = "horses"
    horse_id = Column(Integer, primary_key=True, index=True)
    horse_name = Column(String, unique=True, index=True)

class horseFull(horse):
    coat = Column(Integer)
    current_owner = Column(Integer)