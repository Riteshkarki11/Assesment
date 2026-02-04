from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    education = Column(JSON)
    skills = Column(JSON)
    work_exp = Column(JSON)
    # This was missing and caused your error:
    links = Column(JSON) 

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    tech_stack = Column(JSON)
    links = Column(String)