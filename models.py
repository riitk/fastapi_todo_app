from sqlalchemy import Column, Integer, String, Boolean
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True)
    email = Column(String, unique= True, index = True)
    hashed_password = Column(String)

    # tasks = relationship("Todo", back_populates="owner")

class Todo(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)

    # owner = relationship("User", back_populates="tasks")
