from pydantic import BaseModel
from typing import Optional

class EventCreate(BaseModel):
    user_id: int
    shop_id: int
    product_id: int
    shop_product_id: int
    event_type: str # VIEW, ADD_TO_CART, PURCHASE
    generic_name_id: Optional[int] = None
    category_id: int
    brand_id: Optional[int] = None
    collection_id: Optional[int] = None
    location: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "shop_id": 1,
                "product_id": 101,
                "shop_product_id": 501,
                "event_type": "VIEW",
                "generic_name_id": 10,
                "category_id": 5,
                "brand_id": 3,
                "collection_id": 2,
                "location": "Dhaka, Bangladesh"
            }
        }
