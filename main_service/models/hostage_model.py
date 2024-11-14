from sqlalchemy import Column, Integer, String, ForeignKey, Index, DateTime
from sqlalchemy.orm import relationship

from main_service.models.Base import Base


class HostageModel(Base):
    __tablename__ = 'suspicious_hostage_content'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    sentence_id = Column(Integer, ForeignKey('sentence.id'), nullable=False)
    sentence = Column('Sentence',back_populates="hostage_sentences", nullable=False)
    user = relationship("User", back_populates="hostage_sentences")