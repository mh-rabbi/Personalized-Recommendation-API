from typing import List, Optional
from sqlalchemy import func, desc
from sqlalchemy.orm import Session
from src.domain.entities.events import ShopProductEventEntity, CategoryEventEntity, CollectionEventEntity
from src.domain.repositories.event_repository import EventRepository
from src.infrastructure.database.models import ShopProductEvent, CategoryEvent, CollectionEvent, UserInfo, EventScore

class EventRepositoryImpl(EventRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_shop_product_event(self, event: ShopProductEventEntity) -> ShopProductEventEntity:
        db_event = ShopProductEvent(
            user_id=event.user_id,
            shop_id=event.shop_id,
            product_id=event.product_id,
            shop_product_id=event.shop_product_id,
            generic_name_id=event.generic_name_id,
            category_id=event.category_id,
            brand_id=event.brand_id,
            collection_id=event.collection_id,
            event_id=event.event_id,
            location=event.location,
            timestamp=event.timestamp
        )
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        return event

    def create_category_event(self, event: CategoryEventEntity) -> CategoryEventEntity:
        db_event = CategoryEvent(
            user_id=event.user_id,
            shop_id=event.shop_id,
            shop_product_id=event.shop_product_id,
            category_id=event.category_id,
            event_id=event.event_id,
            location=event.location,
            timestamp=event.timestamp
        )
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        return event

    def create_collection_event(self, event: CollectionEventEntity) -> CollectionEventEntity:
        db_event = CollectionEvent(
            user_id=event.user_id,
            shop_id=event.shop_id,
            shop_product_id=event.shop_product_id,
            collection_id=event.collection_id,
            event_id=event.event_id,
            location=event.location,
            timestamp=event.timestamp
        )
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        return event

    def get_shop_product_events(self, user_id: int, limit: int) -> List[ShopProductEventEntity]:
        events = self.db.query(ShopProductEvent).filter(ShopProductEvent.user_id == user_id).limit(limit).all()
        return [ShopProductEventEntity.model_validate(e) for e in events]

    def get_category_events(self, user_id: int, limit: int) -> List[CategoryEventEntity]:
        events = self.db.query(CategoryEvent).filter(CategoryEvent.user_id == user_id).limit(limit).all()
        return [CategoryEventEntity.model_validate(e) for e in events]

    def get_event_score_by_type(self, event_type: str) -> Optional[int]:
        score_record = self.db.query(EventScore).filter(EventScore.event_type == event_type).first()
        return score_record.id if score_record else None

    def get_top_products_global(self, limit: int) -> List[tuple]:
        return (
            self.db.query(ShopProductEvent.shop_product_id, func.sum(EventScore.score).label("total_score"))
            .join(EventScore, ShopProductEvent.event_id == EventScore.id)
            .group_by(ShopProductEvent.shop_product_id)
            .order_by(desc("total_score"))
            .limit(limit)
            .all()
        )

    def get_top_products_by_segment(self, age_group: str, gender: str, limit: int) -> List[tuple]:
        return (
            self.db.query(ShopProductEvent.shop_product_id, func.sum(EventScore.score).label("total_score"))
            .join(EventScore, ShopProductEvent.event_id == EventScore.id)
            .join(UserInfo, ShopProductEvent.user_id == UserInfo.user_id)
            .filter(UserInfo.age_group == age_group, UserInfo.gender == gender)
            .group_by(ShopProductEvent.shop_product_id)
            .order_by(desc("total_score"))
            .limit(limit)
            .all()
        )

    def get_top_products_by_user(self, user_id: int, limit: int) -> List[tuple]:
        return (
            self.db.query(ShopProductEvent.shop_product_id, func.sum(EventScore.score).label("total_score"))
            .join(EventScore, ShopProductEvent.event_id == EventScore.id)
            .filter(ShopProductEvent.user_id == user_id)
            .group_by(ShopProductEvent.shop_product_id)
            .order_by(desc("total_score"))
            .limit(limit)
            .all()
        )

    def get_top_categories_by_user(self, user_id: int, limit: int) -> List[tuple]:
        return (
            self.db.query(ShopProductEvent.category_id, func.sum(EventScore.score).label("total_score"))
            .join(EventScore, ShopProductEvent.event_id == EventScore.id)
            .filter(ShopProductEvent.user_id == user_id)
            .group_by(ShopProductEvent.category_id)
            .order_by(desc("total_score"))
            .limit(limit)
            .all()
        )

    def get_top_products_by_categories(self, category_ids: List[int], limit: int) -> List[tuple]:
        return (
            self.db.query(ShopProductEvent.shop_product_id, func.sum(EventScore.score).label("total_score"))
            .join(EventScore, ShopProductEvent.event_id == EventScore.id)
            .filter(ShopProductEvent.category_id.in_(category_ids))
            .group_by(ShopProductEvent.shop_product_id)
            .order_by(desc("total_score"))
            .limit(limit)
            .all()
        )

    def get_user_info(self, user_id: int) -> Optional[UserInfo]:
        return self.db.query(UserInfo).filter(UserInfo.user_id == user_id).first()
