"""Product repository implementation using SQLAlchemy."""
from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.product import Product
from src.domain.repositories.product_repository import ProductRepository
from src.infrastructure.database.models import ProductModel


class ProductRepositoryImpl(ProductRepository):
    """Concrete implementation of ProductRepository using SQLAlchemy."""
    
    def __init__(self, db: Session):
        """Initialize repository with database session."""
        self.db = db
    
    def _to_entity(self, model: ProductModel) -> Product:
        """Convert database model to domain entity."""
        return Product(
            id=model.id,
            name=model.name,
            description=model.description,
            price=model.price,
            stock=model.stock,
            created_at=model.created_at,
            updated_at=model.updated_at
        )
    
    def _to_model(self, entity: Product) -> ProductModel:
        """Convert domain entity to database model."""
        return ProductModel(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            price=entity.price,
            stock=entity.stock
        )
    
    def create(self, product: Product) -> Product:
        """Create a new product in the database."""
        db_product = self._to_model(product)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return self._to_entity(db_product)
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        """Get a product by ID from the database."""
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        return self._to_entity(db_product) if db_product else None
    
    def get_all(self, skip: int = 0, limit: int = 100) -> List[Product]:
        """Get all products with pagination."""
        db_products = self.db.query(ProductModel).offset(skip).limit(limit).all()
        return [self._to_entity(p) for p in db_products]
    
    def update(self, product_id: int, product: Product) -> Optional[Product]:
        """Update an existing product."""
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if not db_product:
            return None
        
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.stock = product.stock
        
        self.db.commit()
        self.db.refresh(db_product)
        return self._to_entity(db_product)
    
    def delete(self, product_id: int) -> bool:
        """Delete a product by ID."""
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if not db_product:
            return False
        
        self.db.delete(db_product)
        self.db.commit()
        return True
