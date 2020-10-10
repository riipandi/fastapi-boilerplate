from fastapi import APIRouter
from resources import welcome
from starlette.responses import RedirectResponse

router = APIRouter()
router.include_router(welcome.router, tags=["welcome"], prefix="/v1")

# Redirect to curretn API version
@router.get("/")
async def redirect():
    return RedirectResponse("/v1")
