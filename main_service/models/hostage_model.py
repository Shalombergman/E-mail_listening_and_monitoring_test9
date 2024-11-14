from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class HostageModel(Base):
    __tablename__ = 'suspicious_hostage_content'
    id = Column(Integer, primary_key=True)
