
from sqlalchemy import Column, Integer, String, ForeignKey, Index, Float, DateTime
from sqlalchemy.orm import relationship
from main_service.models.Base import Base



class ExplosiveModel(Base):
    __tablename__ = 'suspicious_explosive_content'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    sentence_id = Column(Integer, ForeignKey('sentence.id'), nullable=False)
    sentence = Column('Sentence', back_populates="explosive_sentences", nullable=False)
    user = relationship("User", back_populates="explosive_sentences")