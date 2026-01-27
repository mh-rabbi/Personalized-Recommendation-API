"""API dependencies."""
from fastapi import Depends
from sqlalchemy.orm import Session
from src.infrastructure.database.config import get_db
from src.infrastructure.repositories.product_repository_impl import ProductRepositoryImpl
from src.application.use_cases.product_use_cases import ProductUseCases


def get_product_repository(db: Session = Depends(get_db)) -> ProductRepositoryImpl:
    """Dependency for ProductRepository."""
    return ProductRepositoryImpl(db)


def get_product_use_cases(
    repository: ProductRepositoryImpl = Depends(get_product_repository)
) -> ProductUseCases:
    """Dependency for ProductUseCases."""
    return ProductUseCases(repository)
