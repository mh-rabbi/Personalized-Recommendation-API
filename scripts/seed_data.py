import sys
import os
import random
from datetime import datetime, timedelta

# Add src to python path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from src.infrastructure.database.config import SessionLocal, init_db
from src.infrastructure.database.models import UserInfo, EventScore, ShopProductEvent, ProductModel

def seed_data():
    db = SessionLocal()
    
    print("Initializing database...")
    init_db()

    print("Seeding Event Scores...")
    scores = [
        {"event_type": "VIEW", "score": 2},
        {"event_type": "ADD_TO_CART", "score": 5},
        {"event_type": "PURCHASE", "score": 10},
    ]
    for s in scores:
        exists = db.query(EventScore).filter_by(event_type=s["event_type"]).first()
        if not exists:
            db.add(EventScore(**s))
    db.commit()

    print("Seeding Users...")
    users = []
    locations = ["Dhaka", "Chittagong", "Sylhet", "Rajshahi", "Khulna"]
    age_groups = ["18-24", "25-34", "35-44", "45-54", "55+"]
    genders = ["Male", "Female"]

    for i in range(1, 51):
        users.append({
            "user_id": i,
            "age_group": random.choice(age_groups),
            "gender": random.choice(genders),
            "location": random.choice(locations)
        })

    for u in users:
        exists = db.query(UserInfo).filter_by(user_id=u["user_id"]).first()
        if not exists:
            db.add(UserInfo(**u))
    db.commit()

    print("Seeding Products...")
    # Seed 100 products across 5 shops
    for i in range(1, 101):
        pid = 100 + i
        shop_id = random.randint(1, 5) # 5 Shops
        exists = db.query(ProductModel).filter_by(id=pid).first()
        if not exists:
            db.add(ProductModel(
                id=pid,
                shop_id=shop_id,
                name=f"Product {i}",
                description=f"Description for product {i} in Shop {shop_id}",
                price=float(random.randint(10, 500)),
                stock=random.randint(10, 200)
            ))
    db.commit()

    print("Seeding Events...")
    event_scores = {s.event_type: s.id for s in db.query(EventScore).all()}
    
    events = []
    # Generate 1000 events
    for _ in range(1000):
        # Pick a random user
        user_id = random.randint(1, 50)
        
        # Pick a product - bias towards first 20 products to make them "Popular"
        if random.random() < 0.6:
            pid = random.randint(101, 120)
        else:
            pid = random.randint(121, 200)
            
        # Get product's shop (need simple look up or just query, but query in loop is slow. 
        # Simplified: We know PID 100+i. We don't strictly enforce shop_id consistency in event 
        # vs product table for this simple seed unless we look it up.
        # Let's trust logic or fetch it. Fetching 1000 times is fine for seeding.
        # Actually, let's just make shop_id consistent by simple math or query.
        # For speed/simplicity in this script:
        # We didn't save product map. Let's just random it or be roughly correct.
        # Real app needs consistency. Let's query product to be safe.
        pass

    # Batch fetch products to map ID -> Shop/Category
    products = db.query(ProductModel).all()
    p_map = {p.id: p.shop_id for p in products}

    for _ in range(1000):
        user_id = random.randint(1, 50)
        
        # Bias
        if random.random() < 0.7:
             pid = random.randint(101, 120) # Popular set
        else:
             pid = random.randint(101, 200) # Full set
        
        if pid not in p_map: continue

        shop_id = p_map[pid]
        
        # Event Type
        rand = random.random()
        if rand < 0.7:
             etype = "VIEW"
        elif rand < 0.9:
             etype = "ADD_TO_CART"
        else:
             etype = "PURCHASE"

        events.append({
            "user_id": user_id,
            "shop_id": shop_id,
            "product_id": pid, 
            "shop_product_id": pid,
            "category_id": random.randint(1, 10), # Random category
            "event_id": event_scores[etype],
            "timestamp": datetime.utcnow() - timedelta(days=random.randint(0, 60))
        })

    for e in events:
        db.add(ShopProductEvent(**e))
    
    db.commit()
    print("Seeding complete!")
    db.close()

if __name__ == "__main__":
    seed_data()
