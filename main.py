from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from handlers import router
from database import db
from config import BOT_TOKEN
import asyncio

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dispatcher = Dispatcher()

async def main():
    dispatcher.include_router(router)

    await db.create_all_tables()
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
