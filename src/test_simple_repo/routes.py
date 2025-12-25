"""API routes for test-simple-repo."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1", tags=["api"])


class Item(BaseModel):
    """Item model."""

    id: int
    name: str
    description: str | None = None


class ItemCreate(BaseModel):
    """Item creation model."""

    name: str
    description: str | None = None


# In-memory storage for demo
_items: dict[int, Item] = {}
_next_id = 1


@router.get("/items")
async def list_items() -> list[Item]:
    """List all items."""
    return list(_items.values())


@router.get("/items/{item_id}")
async def get_item(item_id: int) -> Item:
    """Get an item by ID."""
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    return _items[item_id]


@router.post("/items", status_code=201)
async def create_item(item: ItemCreate) -> Item:
    """Create a new item."""
    global _next_id
    new_item = Item(id=_next_id, name=item.name, description=item.description)
    _items[_next_id] = new_item
    _next_id += 1
    return new_item
