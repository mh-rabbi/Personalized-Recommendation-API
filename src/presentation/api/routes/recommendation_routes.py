from typing import List, Any, Optional
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
    shop_id: Optional[int] = None,
    service: RecommendationService = Depends(get_recommendation_service)
):
    """Get personalized recommendations for a user.
    
    Logic:
    - Case 1: No History -> 100% Segment Popularity (Age/Gender)
    - Case 2: History -> 50% Personal, 30% Category Affinity, 20% Global
    """
    return service.get_personalized_recommendations(user_id, limit, shop_id)

@router.get("/popular/global")
def get_global_popular(
    limit: int = 10,
    shop_id: Optional[int] = None,
    service: RecommendationService = Depends(get_recommendation_service)
):
    """Get global popular products based on engagement score."""
    # Since RecommendationService.get_personalized_recommendations includes global logic,
    # we can expose a dedicated method in Service or reuse logic.
    # For now, let's assume we can fetch global via service helper (which we added implicitly in logic)
    # We should add a specific simple method to service if needed, or query repo directly via service wrapper.
    # Actually, let's use the 'global' part of the logic via a new service method or just reuse the 'best sellers' if similar.
    # But "Popular" != "Best Seller" (Engagement vs Purchase). 
    # Let's add a simple wrapper in Service if missing or just use trending with long duration.
    # For simplicity, treating "Popular" as Trending (Last 30 days) or All Time.
    # Let's use Trending with a very long duration effectively or just add a method.
    # For now, I'll use trending with 365 days as 'Popular' or add 'get_popular_global' to service.
    # I already added get_trending_products. Let's use that for "Popular" if strictly needed or just Global Top.
    # I will call get_top_products_global from repo via a new service method if I want to be clean.
    # But I missed adding explicit `get_popular` to RecommendationService.
    # I'll use trending with 30 days default as implied by 'Popular' usually being recent, or change to call repo directly.
    # To be clean: I will just use trending for now or best sellers.
    # Wait, the task asked for "Popular Shop Products".
    # I implemented get_trending_products.
    
    # Let's use get_trending_products(days=365) to simulate 'Global Popular' for now.
    return service.get_trending_products(limit, days=365, shop_id=shop_id)

@router.get("/trending")
def get_trending_products(
    limit: int = 10,
    days: int = 30,
    shop_id: Optional[int] = None,
    service: RecommendationService = Depends(get_recommendation_service)
):
    """Get trending products (high engagement in last N days)."""
    return service.get_trending_products(limit, days, shop_id)

@router.get("/best-sellers")
def get_best_sellers(
    limit: int = 10,
    shop_id: Optional[int] = None,
    service: RecommendationService = Depends(get_recommendation_service)
):
    """Get best selling products (most purchased)."""
    return service.get_best_sellers(limit, shop_id)
