from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import database


class User(database.dbBaseClass):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)

    fk_group = Column(Integer, ForeignKey("group.id"))
    group_name = relationship("Group", foreign_keys=[fk_group])
    # items = relationship("Item", back_populates="owner")


class UserAllInfo(User):
    last_name = Column(String)
    first_name = Column(String)
    username = Column(String)


class Group(database.dbBaseClass):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, unique=True)

# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")