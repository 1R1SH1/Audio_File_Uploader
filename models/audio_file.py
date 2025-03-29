from sqlalchemy import Column, Integer, String, DateTime, text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AudioFile(Base):
    __tablename__ = "audio_file"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    filename = Column(String, nullable=False)
    path = Column(String, nullable=False)
    uploaded_at = Column(DateTime, server_default=text("now()"))