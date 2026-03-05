from typing import List, Dict, Any, Optional
from src.domain.repositories.event_repository import EventRepository

class RecommendationService:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    def get_personalized_recommendations(self, user_id: int, limit: int = 10, shop_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Get recommendations based on user history.
        Case 1: No History -> 100% Segment Popularity
        Case 2: History -> 50% Personal, 30% Category, 20% Global
        """
        user_history = self.event_repo.get_top_products_by_user(user_id, 1, shop_id=shop_id)
        has_history = len(user_history) > 0
        
        user_info = self.event_repo.get_user_info(user_id)
        # Default segment if missing
        age_group = user_info.age_group if user_info else "25-34"
        gender = user_info.gender if user_info else "Male"

        final_recommendations = []
        seen_product_ids = set()

        if not has_history:
            # Case 1: 100% Segment
            segment_products = self.event_repo.get_top_products_by_segment(age_group, gender, limit, shop_id=shop_id)
            for pid, score in segment_products:
                if pid not in seen_product_ids:
                    final_recommendations.append({"shop_product_id": pid, "score": score, "source": "segment"})
                    seen_product_ids.add(pid)
        else:
            # Case 2: 50/30/20 Split
            limit_personal = int(limit * 0.5)
            limit_category = int(limit * 0.3)
            # Global gets the rest plus any remainder
            limit_global = limit - limit_personal - limit_category 

            # 1. Personal Top Products
            personal_products = self.event_repo.get_top_products_by_user(user_id, limit_personal, shop_id=shop_id)
            for pid, score in personal_products:
                if pid not in seen_product_ids:
                     final_recommendations.append({"shop_product_id": pid, "score": score, "source": "personal"})
                     seen_product_ids.add(pid)
            
            # 2. Category Affinity Products
            # Get top categories for user
            top_categories = self.event_repo.get_top_categories_by_user(user_id, 5, shop_id=shop_id) # Get top 5 categories
            if top_categories:
                category_ids = [c[0] for c in top_categories]
                category_products = self.event_repo.get_top_products_by_categories(category_ids, limit_category * 2, shop_id=shop_id) # Fetch more to filtering duplicates
                
                count = 0
                for pid, score in category_products:
                    if count >= limit_category:
                        break
                    if pid not in seen_product_ids:
                        final_recommendations.append({"shop_product_id": pid, "score": score, "source": "category_affinity"})
                        seen_product_ids.add(pid)
                        count += 1
            
            # 3. Global Popular Products (Fill the rest)
            # We fetch more to account for duplicates
            remaining_limit = limit - len(final_recommendations)
            if remaining_limit > 0:
                global_products = self.event_repo.get_top_products_global(limit * 2, shop_id=shop_id)
                count = 0
                for pid, score in global_products:
                    if count >= remaining_limit:
                        break
                    if pid not in seen_product_ids:
                        final_recommendations.append({"shop_product_id": pid, "score": score, "source": "global"})
                        seen_product_ids.add(pid)
                        count += 1

        return final_recommendations

    def get_trending_products(self, limit: int = 10, days: int = 30, shop_id: Optional[int] = None) -> List[Dict[str, Any]]:
        products = self.event_repo.get_trending_products(limit, days, shop_id)
        return [{"shop_product_id": p[0], "score": p[1], "source": "trending"} for p in products]

    def get_best_sellers(self, limit: int = 10, shop_id: Optional[int] = None) -> List[Dict[str, Any]]:
        products = self.event_repo.get_best_sellers(limit, shop_id)
        return [{"shop_product_id": p[0], "purchase_count": p[1], "source": "best_seller"} for p in products]
