from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from ..database import dbBaseClass


class disease_base(dbBaseClass):
    __tablename__ = "disease"
    id = Column(Integer, primary_key=True, index=True)
    name_disease = Column(String)

class disease(disease_base):
    description = Column(String)
    is_vaccine = Column(Boolean)

class disease_type(dbBaseClass):
    __tablename__ = "disease_type"
    id = Column(Integer, primary_key=True, index=True)
    type_name = Column(String, unique=True)
