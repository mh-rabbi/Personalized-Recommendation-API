from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventScoreEntity(BaseModel):
    id: int
    event_type: str
    score: int
    
    class Config:
        from_attributes = True

class ShopProductEventEntity(BaseModel):
    user_id: int
    shop_id: int
    product_id: int
    shop_product_id: int
    generic_name_id: Optional[int] = None
    category_id: int
    brand_id: Optional[int] = None
    collection_id: Optional[int] = None
    event_id: int
    location: Optional[str] = None
    timestamp: datetime

    class Config:
        from_attributes = True

class CategoryEventEntity(BaseModel):
    user_id: int
    shop_id: int
    shop_product_id: int
    category_id: int
    event_id: int
    location: Optional[str] = None
    timestamp: datetime

    class Config:
        from_attributes = True

class CollectionEventEntity(BaseModel):
    user_id: int
    shop_id: int
    shop_product_id: int
    collection_id: int
    event_id: int
    location: Optional[str] = None
    timestamp: datetime

    class Config:
        from_attributes = True
