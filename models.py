from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'Movie'
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    title = Column(String, nullable=False, unique=True)
    studios = Column(String, nullable=False)
    producers = Column(String, nullable=False)
    winner = Column(Boolean, nullable=False)