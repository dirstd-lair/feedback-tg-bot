from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
DATABASE_URL = "sqlite+aiosqlite:///database/database.db"
ADMIN_ID_CHAT = -5279863189
ADMIN_USERNAME = "@username"

STARTED_MESSAGE = (
    f"Привет! Это бот для обратной связи с сайта.\n"
    f"Тут вы сможете отправить своё обращение или сообщить об ошибке на сайте"
)

FILLING_MESSAGE_1 = (
    f"Укажите причину вашего обращения:\n"
    f"Пример: не работает кнопка на главной странице"
)
FILLING_MESSAGE_2 = (
    f"Расскажите подробнее о вашей проблеме:\n"
    f"Пример: Когда перехожу на вашу страницу и нажимаю на кнопку ничего не происходит!"
)

SEND_MESSAGE_TO_ADMIN = (
    "Поступило новое обращение от "
    "<a href='tg://tg?id={user_id}'>{first_name}</a>\n\n"
    "Тема: {title}\n"
    "Подробное описание: {description}"
)

MESSAGE_CONTACT = (
    f"Для консультации обратитесь к нашему менеджеру {ADMIN_USERNAME}"
)