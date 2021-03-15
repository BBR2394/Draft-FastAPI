from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from ..database import dbBaseClass, dbEngine
from sqlalchemy.orm import relationship


class medicament_base(dbBaseClass):
    __tablename__ = "medicine"
    id = Column(Integer, primary_key=True, index=True)
    dose = Column(Integer)
    name = Column(String, unique=True)


class medicament(medicament_base):
    dose_max = Column(Integer)
    delay = Column(Integer)
    list_type = Column(ARRAY(Integer)) 

#class medicament_with_type(medicament):
   # lsttype = relationship("medecine_type", back_populates="typemed")


class medecine_type(dbBaseClass):
    __tablename__ = "medecine_type"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, unique=True)
    

#class med_type_plus(medecine_type):
 #   typemed = relationship("medicament_with_type", back_populates="lsttype")

