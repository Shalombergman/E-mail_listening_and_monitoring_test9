
from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ExplosiveModel(Base):
    __tablename__ = 'suspicious_explosive_content'