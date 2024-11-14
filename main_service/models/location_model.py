from sqlalchemy import Column, Integer, String, ForeignKey, Index, Float
from main_service.models.Base import Base


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True,autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city = Column(String,nullable=False)
    country = Column(String,nullable=False)