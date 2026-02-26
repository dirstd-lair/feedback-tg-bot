from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from ..models import Base
from config import DATABASE_URL
from utils.logger import get_logger

from .application import ApplicationAction
from .user import UserAction

class Database:
    def __init__(self):
        self.engine = create_async_engine(DATABASE_URL)
        self.async_session = async_sessionmaker(self.engine, expire_on_commit=False)
        self.logger = get_logger(__name__)

        self.application = ApplicationAction(self)
        self.user = UserAction(self)

    async def create_all_tables(self) -> bool:
        async with self.engine.begin() as session:
            try:
                await session.run_sync(Base.metadata.create_all)
                self.logger.info(f"Таблицы успешно созданы. Бот запущен")
            except Exception as ex:
                self.logger.exception(f"Не удалось создать таблицы {ex}")
                exit()