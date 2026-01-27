"""Product repository interface - Abstract repository pattern."""
from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.product import Product


class ProductRepository(ABC):
    """Abstract repository interface for Product operations."""
    
    @abstractmethod
    def create(self, product: Product) -> Product:
        """Create a new product."""
        pass
    
    @abstractmethod
    def get_by_id(self, product_id: int) -> Optional[Product]:
        """Get a product by ID."""
        pass
    
    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Product]:
        """Get all products with pagination."""
        pass
    
    @abstractmethod
    def update(self, product_id: int, product: Product) -> Optional[Product]:
        """Update an existing product."""
        pass
    
    @abstractmethod
    def delete(self, product_id: int) -> bool:
        """Delete a product by ID."""
        pass
