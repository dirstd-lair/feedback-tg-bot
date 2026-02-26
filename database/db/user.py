from sqlalchemy import select
from ..models import User
from utils.logger import get_logger
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .main import Database

class UserAction:
    def __init__(self, db: "Database"):
        self.db = db
        self.logger = get_logger(__name__)

    async def create_user(self, user_id: int) -> User|None:
        async with self.db.async_session() as session:
            try:
                user = User(
                    user_id=user_id
                )
                session.add(user)
                await session.commit()
                await session.refresh(user)
                return user
            except Exception as ex:
                self.logger.exception(f"Не удалось создать пользователя {ex}")

    async def user_register(self, user_id: int) -> bool:
        async with self.db.async_session() as session:
            try:
                user = await session.execute(
                    select(User).where(User.user_id == user_id)
                )
                return user.scalar_one_or_none()
            except Exception as ex:
                self.logger.exception(f"Не удалось проверить пользователя в бд {ex}")