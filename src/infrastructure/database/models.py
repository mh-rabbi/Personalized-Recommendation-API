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


class UserInfo(Base):
    """SQLAlchemy model for User Info."""
    __tablename__ = "user_info"

    user_id = Column(Integer, primary_key=True, index=True) # Assuming external user ID or auto-inc
    age_group = Column(String(50))
    gender = Column(String(50))
    location = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)


class EventScore(Base):
    """SQLAlchemy model for Event Scores."""
    __tablename__ = "event_scores"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String(50), unique=True, index=True) # VIEW, ADD_TO_CART, PURCHASE
    score = Column(Integer, nullable=False)


class ShopProductEvent(Base):
    """SQLAlchemy model for Shop Product Events."""
    __tablename__ = "shop_product_events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    shop_id = Column(Integer, index=True)
    product_id = Column(Integer, index=True)
    shop_product_id = Column(Integer, index=True)
    generic_name_id = Column(Integer, nullable=True)
    category_id = Column(Integer, index=True)
    brand_id = Column(Integer, nullable=True)
    collection_id = Column(Integer, nullable=True)
    event_id = Column(Integer, index=True) # References EventScore.id or just an ID
    timestamp = Column(DateTime, default=datetime.utcnow)
    location = Column(String(255), nullable=True)


class CategoryEvent(Base):
    """SQLAlchemy model for Category Events."""
    __tablename__ = "category_events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    shop_id = Column(Integer, index=True)
    shop_product_id = Column(Integer, index=True)
    category_id = Column(Integer, index=True)
    event_id = Column(Integer, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    location = Column(String(255), nullable=True)


class CollectionEvent(Base):
    """SQLAlchemy model for Collection Events."""
    __tablename__ = "collection_events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    shop_id = Column(Integer, index=True)
    shop_product_id = Column(Integer, index=True)
    collection_id = Column(Integer, index=True)
    event_id = Column(Integer, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    location = Column(String(255), nullable=True)
