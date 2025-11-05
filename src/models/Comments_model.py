from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.settings.database import Base

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    author_name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    
    user = relationship("User", back_populates="comments")
    movie = relationship("Movie", back_populates="comments")
    
    def __repr__(self):
        return f"<Comment(author={self.author_name}, movie_id={self.movie_id})>"
    
    