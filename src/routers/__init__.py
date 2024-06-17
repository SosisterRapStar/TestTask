from fastapi.routing import APIRouter
from .category import cat_router
from .items import item_router

router = APIRouter()


router.include_router(router=cat_router, prefix="/categories")
router.include_router(router=item_router, prefix="/items")