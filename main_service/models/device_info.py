from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class DeviceInfoModel(Base):
    __tablename__ = 'device_info'
    id = Column(Integer, primary_key=True)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)