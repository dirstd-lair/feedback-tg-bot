from aiogram import Router
from .application import router as app_router
from .start import router as start_router

router = Router()
router.include_routers(start_router, app_router)