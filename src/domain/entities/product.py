"""Product entity - Core domain model."""
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Product:
    """Product entity representing a product in the system."""
    
    name: str
    description: str
    price: float
    stock: int
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def __post_init__(self):
        """Validate product data."""
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative")
        if not self.name or not self.name.strip():
            raise ValueError("Product name is required")
