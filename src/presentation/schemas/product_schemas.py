"""Pydantic models for Product API."""
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    """Base Pydantic model for Product."""
    name: str = Field(..., min_length=1, max_length=255, description="The name of the product")
    description: str = Field(..., max_length=1000, description="Description of the product")
    price: float = Field(..., ge=0, description="Price of the product")
    stock: int = Field(..., ge=0, description="Stock quantity")


class ProductCreate(ProductBase):
    """Schema for creating a product."""
    pass


class ProductUpdate(ProductBase):
    """Schema for updating a product."""
    pass


class ProductResponse(ProductBase):
    """Schema for product response."""
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
