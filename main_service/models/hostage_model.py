from sqlalchemy import Column, Integer, String, ForeignKey, Index, DateTime
from main_service.models.Base import Base


class HostageModel(Base):
    __tablename__ = 'suspicious_hostage_content'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime)
    location_id = Column(Integer, ForeignKey('locations.id'))
    device_info = Column(Integer, ForeignKey('devices.id'))
    sentences = Column(Integer, ForeignKey('sentences.id'))