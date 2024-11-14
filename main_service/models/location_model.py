from sqlalchemy import Column, Integer, String, ForeignKey, Index, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String)
    country = Column(String)