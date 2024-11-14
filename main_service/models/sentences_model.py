from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from main_service.models.Base import Base


class SentenceModel(Base):
    __tablename__ = 'sentences'
    id = Column(Integer, primary_key=True)
    sentence = Column(String)

    hostage_sentences = relationship("HostageSentence", back_populates="sentence")
    explosive_sentences = relationship("ExplosiveSentence", back_populates="sentence")