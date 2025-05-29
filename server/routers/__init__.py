from fastapi import APIRouter
from server.routers.chat_router import chat
from server.routers.data_router import data
from server.routers.base_router import base
from server.routers.tool_router import tool
from server.routers.admin_router import admin

router = APIRouter()
router.include_router(base)
router.include_router(chat)
router.include_router(data)
router.include_router(tool)
router.include_router(admin)
