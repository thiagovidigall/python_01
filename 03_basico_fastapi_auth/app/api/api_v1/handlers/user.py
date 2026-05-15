from fastapi import APIRouter
from models.user_model import User

user_router = APIRouter()

@user_router.get("/test")
async def test():
    return "testando rota de users"