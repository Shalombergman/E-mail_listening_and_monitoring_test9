from uuid import uuid4

from sqlalchemy import Column, Integer, String, ForeignKey, Index

from sqlalchemy.orm import relationship

from main_service.models.Base import Base


class DeviceInfoModel(Base):
    __tablename__ = 'device_info'
    id = Column(Integer, primary_key=True)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)
    user = relationship('UserModel', back_populates='device_info', uselist=False)