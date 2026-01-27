"""Product API routes."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from src.application.use_cases.product_use_cases import ProductUseCases
from src.presentation.schemas.product_schemas import ProductCreate, ProductResponse, ProductUpdate
from src.presentation.api.dependencies import get_product_use_cases

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate,
    use_cases: ProductUseCases = Depends(get_product_use_cases)
):
    """Create a new product."""
    try:
        return use_cases.create_product(
            name=product.name,
            description=product.description,
            price=product.price,
            stock=product.stock
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=List[ProductResponse])
def list_products(
    skip: int = 0, 
    limit: int = 100,
    use_cases: ProductUseCases = Depends(get_product_use_cases)
):
    """List products with pagination."""
    return use_cases.list_products(skip=skip, limit=limit)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    use_cases: ProductUseCases = Depends(get_product_use_cases)
):
    """Get a specific product by ID."""
    product = use_cases.get_product(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductUpdate,
    use_cases: ProductUseCases = Depends(get_product_use_cases)
):
    """Update a product."""
    updated_product = use_cases.update_product(
        product_id=product_id,
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )
    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return updated_product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    use_cases: ProductUseCases = Depends(get_product_use_cases)
):
    """Delete a product."""
    success = use_cases.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
