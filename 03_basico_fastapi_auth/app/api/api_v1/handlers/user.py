from fastapi import APIRouter, HTTPException, status
from schema.user_schema import UserAuth
from service.user_service import UserService
import pymongo

user_router = APIRouter()

# @user_router.post("/adicionar", summary="Adicionar usuário", status_code=status.HTTP_201_CREATED)
# async def add_user(user: UserAuth, background_tasks: BackgroundTasks):
#     try:
#         user_in_db = await UserService.create_user_db(user)
#         background_tasks.add_task(send_welcome_email, user_in_db.email)
#         return user_in_db

@user_router.post("/adicionar", summary="Adicionar usuário", status_code=status.HTTP_201_CREATED)
async def add_user(user: UserAuth):
    try:
        return await UserService.create_user_db(user)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário já existe")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))