# 🤖 Site Feedback Telegram Bot

Асинхронный Telegram-бот для сбора обратной связи и сообщений об ошибках с сайта. Построен на современном стеке с полной контейнеризацией.

---

## ⚙️ Конфигурация проекта

Настройка бота осуществляется через файл <code>.env</code> и внутренние константы в коде.

### 1. Переменные окружения (.env)
Создайте файл <code>.env</code> в корне проекта:


| Ключ | Описание |
| :--- | :--- |
| <b>TOKEN</b> | API-токен бота от <a href="https://t.me">@BotFather</a> |

### 2. Внутренние настройки
Основные параметры логики (находятся в <code>config.py</code> или <code>main.py</code>):
* <b>База данных</b>: SQLite (`aiosqlite`). Путь: <code>database/database.db</code>.
* <b>Администрирование</b>:
    * <code>ADMIN_ID_CHAT</code>: <code>-5279863189</code> (ID группы для заявок).
    * <code>ADMIN_USERNAME</code>: <code>@username</code> (менеджер для связи).

---

## 🐳 Запуск через Docker

<details>
<summary><b>▶ Нажмите, чтобы развернуть инструкции по сборке</b></summary>

1. **Сборка образа:**
   <pre><code>docker build -t feedback-bot .</code></pre>

2. **Запуск с сохранением базы данных:**
   <pre><code>docker run -d \
  --name feedback-app \
  --env-file .env \
  -v $(pwd)/database:/app/database \
  feedback-bot</code></pre>

</details>

---

## 🛠 Стек технологий

<table width="100%">
  <tr>
    <td align="center" width="25%">
      <b>Python 3.12</b><br>Core Language
    </td>
    <td align="center" width="25%">
      <b>Aiogram 3</b><br>Bot Framework
    </td>
    <td align="center" width="25%">
      <b>Aiosqlite</b><br>Async DB
    </td>
    <td align="center" width="25%">
      <b>Docker</b><br>Containerization
    </td>
  </tr>
</table>

---

<p align="center">
  <b>Разработано для эффективной обратной связи</b><br>
  <sub>Автор: <a href="https://t.me">@dirstd</a></sub>
</p>
