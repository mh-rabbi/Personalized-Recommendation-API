"""SQLAlchemy database models."""
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from src.infrastructure.database.config import Base


class ProductModel(Base):
    """SQLAlchemy model for Product table."""
    
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(String(1000), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
