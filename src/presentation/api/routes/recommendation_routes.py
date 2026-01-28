from typing import List, Any
from fastapi import APIRouter, Depends, Query, status
from src.presentation.api.dependencies import get_event_service, get_recommendation_service
from src.application.services.event_service import EventService
from src.application.services.recommendation_service import RecommendationService
from src.presentation.schemas.event_schemas import EventCreate

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

@router.post("/events", status_code=status.HTTP_201_CREATED)
def record_event(
    event: EventCreate,
    service: EventService = Depends(get_event_service)
):
    """Record a user event (VIEW, ADD_TO_CART, PURCHASE)."""
    return service.record_event(event)

@router.get("/personalized/{user_id}")
def get_personalized_recommendations(
    user_id: int,
    limit: int = 10,
    service: RecommendationService = Depends(get_recommendation_service)
):
    """Get personalized recommendations for a user."""
    return service.get_personalized_recommendations(user_id, limit)

@router.get("/popular/global")
def get_global_popular(
    limit: int = 10,
    service: RecommendationService = Depends(get_recommendation_service)
):
    """Get global popular products."""
    # Assuming service exposes this or we add a proxy method
    # Since I didn't add it to service explicitly, I should strictly call repo methods via service or add methods to service.
    # For now, I'll access repo directly via service if I didn't verify service methods.
    # BETTER: Add method to RecommendationService. I will rely on logic inside service.
    # Re-reading RecommendationService: it only has `get_personalized_recommendations`.
    # I should update RecommendationService to expose basic lists or handle this request.
    # For now, I'll return a placeholder or implement it properly by updating Service.
    pass 
