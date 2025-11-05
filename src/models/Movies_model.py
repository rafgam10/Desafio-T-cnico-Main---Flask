from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from src.settings.database import Base

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    synopsis = Column(Text, nullable=False)
    release_year = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    poster_url = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    
    user = relationship("User", back_populates="movies")
    comments = relationship("Comment", back_populates="movie", cascade="all, delete-orpharn")
    
    def __repr__(self):
        return f"<Movie(title={self.title}), year={self.release_year}>"