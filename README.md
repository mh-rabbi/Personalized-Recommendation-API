# 🎯 Personalized Recommendation API

<div align="center">

[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.25-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.5.3-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://pydantic-docs.helpmanual.io/)

**Intelligent Product Recommendation Engine with Clean Architecture**

[Features](#-features) • [Installation](#-installation) • [API Documentation](#-api-documentation) • [Architecture](#-architecture) • [Usage](#-usage)

</div>

---

## 📋 Overview

A production-ready, scalable recommendation API built with FastAPI following Clean Architecture principles. This system provides intelligent, personalized product recommendations based on user behavior, demographics, and engagement patterns.

### 🎯 Key Highlights

- 🏗️ **Clean Architecture** - Separation of concerns with domain, application, infrastructure, and presentation layers
- 🤖 **Smart Recommendations** - Multi-strategy recommendation engine (Personal, Segment, Category Affinity, Global)
- 📊 **Event Tracking** - Comprehensive user behavior tracking (VIEW, ADD_TO_CART, PURCHASE)
- 🎭 **Demographic Targeting** - Age group and gender-based recommendations
- 🔥 **Real-time Analytics** - Trending products and best sellers
- 🚀 **High Performance** - Optimized SQL queries with aggregations
- 📈 **Scalable Design** - Multi-shop support with filtering
- 🔌 **RESTful API** - Well-documented endpoints with OpenAPI/Swagger

---

## ✨ Features

### 🎯 Recommendation Strategies

#### **1. Personalized Recommendations**
Adaptive algorithm that combines multiple signals:

- **No History Users (Cold Start)**
  - 100% Segment-Based Popularity (Age Group + Gender)
  - Example: 25-34 Male in Dhaka sees popular products among similar users

- **Users with History**
  - 50% Personal Preferences (User's top interacted products)
  - 30% Category Affinity (Products from user's favorite categories)
  - 20% Global Trending (Overall popular products)

#### **2. Trending Products**
- Time-based popularity (default: last 30 days)
- Weighted scoring by event type:
  - VIEW: 2 points
  - ADD_TO_CART: 5 points
  - PURCHASE: 10 points
- Real-time engagement tracking

#### **3. Best Sellers**
- Purchase-based ranking
- Actual conversion metrics
- Shop-specific filtering

#### **4. Global Popular Products**
- All-time engagement leaders
- Cross-shop popularity
- Weighted by engagement scores

### 📊 Event Tracking System

- **VIEW Events** - Product page visits
- **ADD_TO_CART Events** - Items added to shopping cart
- **PURCHASE Events** - Completed transactions
- Automatic scoring and weighting
- Timestamp tracking for temporal analysis
- Location-based event logging

### 🎭 Demographic Intelligence

- **Age Group Segmentation** (18-24, 25-34, 35-44, 45-54, 55+)
- **Gender-Based Recommendations**
- **Location Targeting** (City/Region level)
- **Combined Segment Analysis**

### 🏪 Multi-Shop Support

- Shop-specific recommendations
- Shop-level filtering across all endpoints
- Product isolation per shop
- Cross-shop global trends

---

## 🛠️ Tech Stack

### Backend Framework
- **FastAPI 0.109.0** - Modern, high-performance web framework
- **Uvicorn[standard] 0.27.0** - ASGI server with HTTP/2 support
- **Python 3.8+** - Programming language

### Database & ORM
- **SQLAlchemy 2.0.25** - SQL toolkit and ORM
- **SQLite** - Default database (easily swappable to PostgreSQL/MySQL)

### Data Validation
- **Pydantic 2.5.3** - Data validation using Python type hints
- **Pydantic Settings 2.1.0** - Settings management

### Configuration
- **Python-dotenv 1.0.0** - Environment variable management

---

## 📦 Installation

### Prerequisites

- **Python** >= 3.8
- **pip** >= 21.0
- **Virtual Environment** (recommended)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/recommendation-api.git
   cd recommendation-api
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate on Linux/Mac
   source venv/bin/activate

   # Activate on Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```

   Edit `.env` with your configuration:
   ```env
   DATABASE_URL=sqlite:///./products.db
   # For PostgreSQL: postgresql://user:password@localhost/dbname
   # For MySQL: mysql://user:password@localhost/dbname
   ```

5. **Initialize database**
   ```bash
   # Database tables are created automatically on first run
   # Or manually initialize:
   python -c "from src.infrastructure.database.config import init_db; init_db()"
   ```

6. **Seed sample data (optional)**
   ```bash
   python scripts/seed_data.py
   ```
   
   This creates:
   - 50 sample users with demographics
   - 100 products across 5 shops
   - 1000 sample events
   - Event score configuration (VIEW: 2, ADD_TO_CART: 5, PURCHASE: 10)

7. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

8. **Access the API**
   ```
   http://localhost:8000
   ```

---

## 📚 API Documentation

### Interactive Documentation

Once the server is running, access:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### API Endpoints

#### **Health Check**

```http
GET /
```

Response:
```json
{
  "status": "ok",
  "message": "Service is running"
}
```

---

#### **Product Management**

##### **Create Product**
```http
POST /api/v1/products
```

Request Body:
```json
{
  "name": "Samsung Galaxy S24",
  "description": "Latest flagship smartphone with AI features",
  "price": 999.99,
  "stock": 50
}
```

Response: `201 Created`
```json
{
  "id": 1,
  "name": "Samsung Galaxy S24",
  "description": "Latest flagship smartphone with AI features",
  "price": 999.99,
  "stock": 50,
  "created_at": "2024-03-05T10:30:00",
  "updated_at": "2024-03-05T10:30:00"
}
```

##### **List Products**
```http
GET /api/v1/products?skip=0&limit=100
```

##### **Get Product**
```http
GET /api/v1/products/{product_id}
```

##### **Update Product**
```http
PUT /api/v1/products/{product_id}
```

##### **Delete Product**
```http
DELETE /api/v1/products/{product_id}
```

---

#### **Event Tracking**

##### **Record Event**
```http
POST /api/v1/recommendations/events
```

Request Body:
```json
{
  "user_id": 1,
  "shop_id": 1,
  "product_id": 101,
  "shop_product_id": 501,
  "event_type": "VIEW",
  "category_id": 5,
  "brand_id": 3,
  "collection_id": 2,
  "location": "Dhaka, Bangladesh"
}
```

**Event Types:**
- `VIEW` - Product viewed (2 points)
- `ADD_TO_CART` - Added to cart (5 points)
- `PURCHASE` - Product purchased (10 points)

Response: `201 Created`

---

#### **Recommendation Endpoints**

##### **Personalized Recommendations**
```http
GET /api/v1/recommendations/personalized/{user_id}?limit=10&shop_id=1
```

**Query Parameters:**
- `user_id` (required) - User ID
- `limit` (optional) - Number of recommendations (default: 10)
- `shop_id` (optional) - Filter by specific shop

Response:
```json
[
  {
    "shop_product_id": 105,
    "score": 45.0,
    "source": "personal"
  },
  {
    "shop_product_id": 112,
    "score": 38.5,
    "source": "category_affinity"
  },
  {
    "shop_product_id": 203,
    "score": 120.0,
    "source": "global"
  }
]
```

**Recommendation Sources:**
- `personal` - Based on user's own history
- `category_affinity` - From user's favorite categories
- `segment` - Based on demographic segment
- `global` - Overall popular products

##### **Global Popular Products**
```http
GET /api/v1/recommendations/popular/global?limit=10&shop_id=1
```

Response:
```json
[
  {
    "shop_product_id": 105,
    "score": 850.0,
    "source": "trending"
  }
]
```

##### **Trending Products**
```http
GET /api/v1/recommendations/trending?limit=10&days=30&shop_id=1
```

**Query Parameters:**
- `limit` - Number of products (default: 10)
- `days` - Time window in days (default: 30)
- `shop_id` - Filter by shop (optional)

##### **Best Sellers**
```http
GET /api/v1/recommendations/best-sellers?limit=10&shop_id=1
```

Response:
```json
[
  {
    "shop_product_id": 108,
    "purchase_count": 47,
    "source": "best_seller"
  }
]
```

---

## 🏗️ Architecture

### Clean Architecture Layers

```
┌─────────────────────────────────────────────────────────┐
│                   Presentation Layer                     │
│  (API Routes, Schemas, Dependencies)                    │
│  - FastAPI endpoints                                     │
│  - Pydantic validation                                   │
│  - Request/Response handling                             │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│                   Application Layer                      │
│  (Use Cases, Services, Business Logic)                  │
│  - ProductUseCases                                       │
│  - EventService                                          │
│  - RecommendationService                                 │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│                     Domain Layer                         │
│  (Entities, Repository Interfaces)                       │
│  - Product Entity                                        │
│  - Event Entities                                        │
│  - Repository Contracts                                  │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│                  Infrastructure Layer                    │
│  (Database, External Services)                           │
│  - SQLAlchemy Models                                     │
│  - Repository Implementations                            │
│  - Database Configuration                                │
└─────────────────────────────────────────────────────────┘
```

### Project Structure

```
recommendation-api/
├── main.py                          # Application entry point
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment template
├── .gitignore                       # Git ignore rules
├── README.md                        # This file
├── scripts/
│   └── seed_data.py                # Database seeding script
└── src/
    ├── domain/                      # Domain Layer
    │   ├── entities/
    │   │   ├── product.py          # Product entity
    │   │   └── events.py           # Event entities
    │   └── repositories/
    │       ├── product_repository.py      # Product repo interface
    │       └── event_repository.py        # Event repo interface
    ├── application/                 # Application Layer
    │   ├── use_cases/
    │   │   └── product_use_cases.py       # Product business logic
    │   └── services/
    │       ├── event_service.py           # Event tracking service
    │       └── recommendation_service.py  # Recommendation engine
    ├── infrastructure/              # Infrastructure Layer
    │   ├── database/
    │   │   ├── config.py           # Database configuration
    │   │   └── models.py           # SQLAlchemy models
    │   └── repositories/
    │       ├── product_repository_impl.py
    │       └── event_repository_impl.py
    └── presentation/                # Presentation Layer
        ├── api/
        │   ├── dependencies.py     # Dependency injection
        │   └── routes/
        │       ├── product_routes.py
        │       └── recommendation_routes.py
        └── schemas/
            ├── product_schemas.py   # Product API schemas
            └── event_schemas.py     # Event API schemas
```

---

## 💾 Database Schema

### Tables

#### **products**
```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    shop_id INTEGER DEFAULT 1,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(1000),
    price FLOAT NOT NULL,
    stock INTEGER DEFAULT 0,
    created_at DATETIME,
    updated_at DATETIME
);
```

#### **user_info**
```sql
CREATE TABLE user_info (
    user_id INTEGER PRIMARY KEY,
    age_group VARCHAR(50),      -- "18-24", "25-34", etc.
    gender VARCHAR(50),          -- "Male", "Female"
    location VARCHAR(255),       -- "Dhaka", "Chittagong", etc.
    created_at DATETIME
);
```

#### **event_scores**
```sql
CREATE TABLE event_scores (
    id INTEGER PRIMARY KEY,
    event_type VARCHAR(50) UNIQUE,  -- VIEW, ADD_TO_CART, PURCHASE
    score INTEGER NOT NULL
);
```

#### **shop_product_events**
```sql
CREATE TABLE shop_product_events (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    shop_id INTEGER,
    product_id INTEGER,
    shop_product_id INTEGER,
    generic_name_id INTEGER,
    category_id INTEGER,
    brand_id INTEGER,
    collection_id INTEGER,
    event_id INTEGER,           -- References event_scores.id
    timestamp DATETIME,
    location VARCHAR(255)
);
```

#### **category_events**
```sql
CREATE TABLE category_events (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    shop_id INTEGER,
    shop_product_id INTEGER,
    category_id INTEGER,
    event_id INTEGER,
    timestamp DATETIME,
    location VARCHAR(255)
);
```

#### **collection_events**
```sql
CREATE TABLE collection_events (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    shop_id INTEGER,
    shop_product_id INTEGER,
    collection_id INTEGER,
    event_id INTEGER,
    timestamp DATETIME,
    location VARCHAR(255)
);
```

### Indexes

- `user_id` - User event lookup
- `shop_id` - Shop filtering
- `product_id`, `shop_product_id` - Product queries
- `category_id` - Category affinity
- `event_id` - Event type filtering
- `timestamp` - Temporal queries

---

## 🎯 Recommendation Algorithm

### Strategy Details

#### **Cold Start (No History)**

```python
# 100% Segment-Based
recommendations = get_top_products_by_segment(
    age_group=user.age_group,
    gender=user.gender,
    limit=10
)
```

**Use Case:** New users, users with no interactions

**Example:**
- User: 25-34, Male, Dhaka
- Shows: Top products viewed/purchased by similar demographic

#### **Warm Start (Has History)**

```python
# 50% Personal
personal = get_top_products_by_user(user_id, limit=5)

# 30% Category Affinity
top_categories = get_top_categories_by_user(user_id, limit=5)
category_products = get_top_products_by_categories(
    category_ids=top_categories,
    limit=3
)

# 20% Global Popular
global_products = get_top_products_global(limit=2)

# Combine and deduplicate
recommendations = personal + category_products + global_products
```

**Use Case:** Active users with interaction history

**Scoring Formula:**
```
Product Score = Σ(event_weight × event_count)

Where:
- VIEW: 2 points
- ADD_TO_CART: 5 points
- PURCHASE: 10 points
```

---

## 🔧 Configuration

### Environment Variables

```env
# Database Configuration
DATABASE_URL=sqlite:///./products.db

# For PostgreSQL
# DATABASE_URL=postgresql://username:password@localhost:5432/dbname

# For MySQL
# DATABASE_URL=mysql://username:password@localhost:3306/dbname

# API Configuration
API_V1_PREFIX=/api/v1
PROJECT_NAME=Recommendation API

# CORS Configuration (optional)
BACKEND_CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]
```

### Database Configuration

To switch databases, update `DATABASE_URL` in `.env`:

**PostgreSQL:**
```bash
pip install psycopg2-binary
# Update DATABASE_URL
DATABASE_URL=postgresql://user:pass@localhost/dbname
```

**MySQL:**
```bash
pip install pymysql
# Update DATABASE_URL
DATABASE_URL=mysql+pymysql://user:pass@localhost/dbname
```

---

## 🚀 Running the Application

### Development Mode

```bash
# With auto-reload
uvicorn main:app --reload

# Custom host and port
uvicorn main:app --host 0.0.0.0 --port 8080 --reload

# With log level
uvicorn main:app --reload --log-level debug
```

### Production Mode

```bash
# With multiple workers
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# With Gunicorn
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

---

## 🧪 Testing the API

### Using cURL

**Record a VIEW event:**
```bash
curl -X POST "http://localhost:8000/api/v1/recommendations/events" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "shop_id": 1,
    "product_id": 101,
    "shop_product_id": 101,
    "event_type": "VIEW",
    "category_id": 5
  }'
```

**Get personalized recommendations:**
```bash
curl "http://localhost:8000/api/v1/recommendations/personalized/1?limit=5"
```

**Get trending products:**
```bash
curl "http://localhost:8000/api/v1/recommendations/trending?limit=10&days=7"
```

### Using Python Requests

```python
import requests

BASE_URL = "http://localhost:8000/api/v1"

# Record event
event_data = {
    "user_id": 1,
    "shop_id": 1,
    "product_id": 101,
    "shop_product_id": 101,
    "event_type": "PURCHASE",
    "category_id": 5
}
response = requests.post(f"{BASE_URL}/recommendations/events", json=event_data)
print(response.json())

# Get recommendations
response = requests.get(f"{BASE_URL}/recommendations/personalized/1?limit=10")
recommendations = response.json()
print(recommendations)
```

### Using HTTPie

```bash
# Record event
http POST :8000/api/v1/recommendations/events \
  user_id:=1 \
  shop_id:=1 \
  product_id:=101 \
  shop_product_id:=101 \
  event_type="VIEW" \
  category_id:=5

# Get recommendations
http GET :8000/api/v1/recommendations/personalized/1 limit==10
```

---

## 📊 Use Cases & Examples

### Example 1: E-commerce Product Recommendations

```python
# User browses electronics
POST /api/v1/recommendations/events
{
  "user_id": 42,
  "shop_id": 1,
  "product_id": 205,
  "shop_product_id": 205,
  "event_type": "VIEW",
  "category_id": 3,  # Electronics
  "location": "Dhaka"
}

# Get personalized recommendations
GET /api/v1/recommendations/personalized/42?limit=5

# Returns: Mix of electronics (category affinity),
# user's previously viewed items, and trending products
```

### Example 2: Multi-Shop Marketplace

```python
# Shop 1: Fashion Store
POST /api/v1/recommendations/events
{
  "user_id": 15,
  "shop_id": 1,
  "product_id": 301,
  "shop_product_id": 301,
  "event_type": "ADD_TO_CART",
  "category_id": 7  # Clothing
}

# Get shop-specific recommendations
GET /api/v1/recommendations/personalized/15?shop_id=1&limit=10

# Returns only products from Shop 1
```

### Example 3: Trending Dashboard

```python
# Get last 7 days trending
GET /api/v1/recommendations/trending?days=7&limit=20

# Get best sellers
GET /api/v1/recommendations/best-sellers?limit=10

# Compare by shop
GET /api/v1/recommendations/trending?shop_id=1&days=7
GET /api/v1/recommendations/trending?shop_id=2&days=7
```

---

## 🔍 Advanced Features

### Query Optimization

The API uses optimized SQL queries with:

- **Aggregations** - `SUM()`, `COUNT()` for scoring
- **Joins** - Efficient joins between events, scores, and users
- **Indexes** - Strategic indexes on frequently queried fields
- **Group By** - Product-level aggregations
- **Limit & Offset** - Pagination support

Example Query:
```sql
SELECT 
    shop_product_id,
    SUM(event_scores.score) as total_score
FROM shop_product_events
JOIN event_scores ON shop_product_events.event_id = event_scores.id
JOIN user_info ON shop_product_events.user_id = user_info.user_id
WHERE 
    user_info.age_group = '25-34' 
    AND user_info.gender = 'Male'
    AND shop_product_events.shop_id = 1
GROUP BY shop_product_id
ORDER BY total_score DESC
LIMIT 10;
```

### Caching Strategy (Future Enhancement)

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_recommendations_cached(user_id: int, limit: int):
    return get_personalized_recommendations(user_id, limit)
```

### Real-time Updates

Events are immediately reflected in recommendations:
1. User action triggers event
2. Event stored with timestamp
3. Next recommendation query includes new data
4. Scores automatically updated via aggregation

---

## 🐛 Troubleshooting

### Common Issues

**1. Database Connection Error**
```bash
# Check database URL
echo $DATABASE_URL

# Reinitialize database
python -c "from src.infrastructure.database.config import init_db; init_db()"
```

**2. Import Errors**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**3. Port Already in Use**
```bash
# Use different port
uvicorn main:app --port 8001

# Or kill existing process
lsof -ti:8000 | xargs kill -9  # Linux/Mac
```

**4. No Recommendations Returned**
```bash
# Seed sample data
python scripts/seed_data.py

# Verify events exist
sqlite3 products.db "SELECT COUNT(*) FROM shop_product_events;"
```

**5. CORS Issues**
```python
# Update main.py CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📈 Performance Considerations

### Optimization Tips

1. **Database Indexes**
   - Add indexes on frequently queried columns
   - Composite indexes for common filter combinations

2. **Connection Pooling**
   ```python
   engine = create_engine(
       DATABASE_URL,
       pool_size=10,
       max_overflow=20
   )
   ```

3. **Query Limits**
   - Always use `LIMIT` to prevent full table scans
   - Implement pagination for large result sets

4. **Caching**
   - Redis for frequently accessed recommendations
   - Cache invalidation on new events

5. **Async Operations** (Future)
   ```python
   from fastapi import BackgroundTasks
   
   @router.post("/events")
   async def record_event(event: EventCreate, background_tasks: BackgroundTasks):
       background_tasks.add_task(process_event, event)
   ```

---

## 🔒 Security Best Practices

### Implemented

- ✅ **Input Validation** - Pydantic schemas
- ✅ **SQL Injection Prevention** - SQLAlchemy ORM
- ✅ **CORS Configuration** - Controlled origins
- ✅ **Environment Variables** - Sensitive data protection

### Recommended Additions

- 🔐 **Authentication** - JWT tokens, OAuth2
- 🔑 **API Keys** - Rate limiting per client
- 🛡️ **HTTPS** - SSL/TLS encryption
- 📝 **Logging** - Audit trails
- 🚫 **Rate Limiting** - Prevent abuse

Example JWT Implementation:
```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

security = HTTPBearer()

def verify_token(credentials = Depends(security)):
    # Implement JWT verification
    pass
```

---

## 🚀 Deployment

### Docker Deployment

**Dockerfile:**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/recommendations
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=recommendations
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Run:**
```bash
docker-compose up -d
```

### Cloud Deployment

**Heroku:**
```bash
heroku create recommendation-api
heroku addons:create heroku-postgresql
git push heroku main
```

**AWS EC2:**
```bash
# Install dependencies
sudo apt update
sudo apt install python3-pip nginx

# Clone and setup
git clone <repo>
pip3 install -r requirements.txt

# Run with systemd
sudo systemctl start recommendation-api
```

**Railway/Render:**
- Connect GitHub repository
- Set environment variables
- Auto-deploy on push

---

## 📊 Monitoring & Logging

### Application Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

@router.get("/recommendations/personalized/{user_id}")
def get_recommendations(user_id: int):
    logger.info(f"Fetching recommendations for user {user_id}")
    # ... logic
    logger.info(f"Returned {len(results)} recommendations")
```

### Metrics (Future)

```python
from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)
# Access metrics at /metrics
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit changes**
   ```bash
   git commit -m 'Add AmazingFeature'
   ```
4. **Push to branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open Pull Request**

### Development Guidelines

- Follow PEP 8 style guide
- Write docstrings for all functions
- Add type hints
- Update tests for new features
- Update documentation

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/mh-rabbi)
- LinkedIn: [Your Profile](https://linkedin.com/in/rabbi221)
- Email: mhr221official@gmail.com

---

## 🙏 Acknowledgments

- **FastAPI** - Modern web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation library
- **Uvicorn** - Lightning-fast ASGI server

---

## 📚 Resources

### Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Clean Architecture Guide](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

### Tutorials

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/tutorial.html)
- [Recommendation Systems](https://developers.google.com/machine-learning/recommendation)

---

## 📞 Support

For issues and questions:

- **GitHub Issues**: [Create an issue](https://github.com/yourusername/recommendation-api/issues)
- **Email**: support@yourapp.com
- **Documentation**: [Full API Docs](http://localhost:8000/docs)

---

<div align="center">

**Built with ❤️ using FastAPI and Clean Architecture**

[⬆ Back to Top](#-personalized-recommendation-api)

</div>
