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


from src.infrastructure.repositories.event_repository_impl import EventRepositoryImpl
from src.application.services.event_service import EventService
from src.application.services.recommendation_service import RecommendationService

def get_event_repository(db: Session = Depends(get_db)) -> EventRepositoryImpl:
    """Dependency for EventRepository."""
    return EventRepositoryImpl(db)

def get_event_service(
    repository: EventRepositoryImpl = Depends(get_event_repository)
) -> EventService:
    """Dependency for EventService."""
    return EventService(repository)

def get_recommendation_service(
    repository: EventRepositoryImpl = Depends(get_event_repository)
) -> RecommendationService:
    """Dependency for RecommendationService."""
    return RecommendationService(repository)
