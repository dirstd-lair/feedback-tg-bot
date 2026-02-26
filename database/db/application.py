from sqlalchemy import select, update
from ..models import Application
from utils.logger import get_logger
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .main import Database

class ApplicationAction:
    def __init__(self, db: "Database"):
        self.db = db
        self.logger = get_logger(__name__)

    async def create_application(self, title: str, description: str, author_id: int) -> Application|None:
        async with self.db.async_session() as session:
          try:
            app = Application(
                title=title,
                description=description,
                author_id=author_id
            )
            session.add(app)
            await session.commit()
            await session.refresh(app)
            return app
          except Exception as ex:
             self.logger.exception(f"Не удалось создать обращение {ex}")


