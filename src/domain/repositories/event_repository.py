from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.events import ShopProductEventEntity, CategoryEventEntity, CollectionEventEntity

class EventRepository(ABC):
    @abstractmethod
    def create_shop_product_event(self, event: ShopProductEventEntity) -> ShopProductEventEntity:
        pass

    @abstractmethod
    def create_category_event(self, event: CategoryEventEntity) -> CategoryEventEntity:
        pass
    
    @abstractmethod
    def create_collection_event(self, event: CollectionEventEntity) -> CollectionEventEntity:
        pass
    
    @abstractmethod
    def get_shop_product_events(self, user_id: int, limit: int) -> List[ShopProductEventEntity]:
        pass

    @abstractmethod
    def get_category_events(self, user_id: int, limit: int) -> List[CategoryEventEntity]:
        pass

    @abstractmethod
    def get_event_score_by_type(self, event_type: str) -> Optional[int]:
        pass

    @abstractmethod
    def get_top_products_global(self, limit: int) -> List[tuple]:
        pass

    @abstractmethod
    def get_top_products_by_segment(self, age_group: str, gender: str, limit: int) -> List[tuple]:
        pass

    @abstractmethod
    def get_top_products_by_user(self, user_id: int, limit: int) -> List[tuple]:
        pass

    @abstractmethod
    def get_top_categories_by_user(self, user_id: int, limit: int) -> List[tuple]:
        pass

    @abstractmethod
    def get_top_products_by_categories(self, category_ids: List[int], limit: int) -> List[tuple]:
        pass

    @abstractmethod
    def get_user_info(self, user_id: int) -> Optional[object]:
        pass
