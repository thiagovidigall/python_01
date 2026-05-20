from models.user_model import User
from schema.user_schema import UserAuth
from core.security import get_password_hash

class UserService:
    # async def create_user(self, user: UserAuth) -> User:
    #     return await User.create(user)
    
    @staticmethod
    async def create_user_db(user: UserAuth):
        user_in_db = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password_hash(user.password)

        )
        await user_in_db.save()
        return user_in_db   

    # async def get_user(self, user_id: UUID) -> User:
    #     return await User.get(user_id)

    # async def update_user(self, user_id: UUID, user: UserAuth) -> User:
    #     return await User.update(user_id, user)

    # async def delete_user(self, user_id: UUID) -> User:
    #     return await User.delete(user_id)