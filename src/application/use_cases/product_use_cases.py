"""Product use cases implementation."""
from typing import List, Optional
from src.domain.entities.product import Product
from src.domain.repositories.product_repository import ProductRepository


class ProductUseCases:
    """Use cases for Product operations."""
    
    def __init__(self, product_repository: ProductRepository):
        """Initialize with product repository."""
        self.product_repository = product_repository
    
    def create_product(self, name: str, description: str, price: float, stock: int) -> Product:
        """Create a new product."""
        product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock
        )
        return self.product_repository.create(product)
    
    def get_product(self, product_id: int) -> Optional[Product]:
        """Get a product by ID."""
        return self.product_repository.get_by_id(product_id)
    
    def list_products(self, skip: int = 0, limit: int = 100) -> List[Product]:
        """List all products."""
        return self.product_repository.get_all(skip, limit)
    
    def update_product(self, product_id: int, name: str, description: str, price: float, stock: int) -> Optional[Product]:
        """Update a product."""
        product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock
        )
        return self.product_repository.update(product_id, product)
    
    def delete_product(self, product_id: int) -> bool:
        """Delete a product."""
        return self.product_repository.delete(product_id)
