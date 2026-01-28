from datetime import datetime
from src.domain.repositories.event_repository import EventRepository
from src.presentation.schemas.event_schemas import EventCreate
from src.domain.entities.events import ShopProductEventEntity

class EventService:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    def record_event(self, event_data: EventCreate):
        # 1. Get Event Score ID
        event_score_id = self.event_repo.get_event_score_by_type(event_data.event_type)
        if not event_score_id:
            # Fallback or Log Error. For now assuming seeded.
            # You might want to auto-create generic scores here if missing
            return None

        # 2. Create ShopProductEvent
        # Assuming we populate ShopProductEvent as the main source of truth
        # since it contains category_id etc.
        
        entity = ShopProductEventEntity(
            user_id=event_data.user_id,
            shop_id=event_data.shop_id,
            product_id=event_data.product_id,
            shop_product_id=event_data.shop_product_id,
            generic_name_id=event_data.generic_name_id,
            category_id=event_data.category_id,
            brand_id=event_data.brand_id,
            collection_id=event_data.collection_id,
            event_id=event_score_id,
            location=event_data.location,
            timestamp=datetime.utcnow()
        )
        
        return self.event_repo.create_shop_product_event(entity)
