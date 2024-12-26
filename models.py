from sqlalchemy import Column, Integer, String
from init import Base

class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    eng = Column(String, nullable=False)
    rus = Column(String, nullable=False)
