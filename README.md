# 🤖 Site Feedback Telegram Bot

<p align="left">
  <img src="https://img.shields.io">
  <img src="https://img.shields.io">
  <img src="https://img.shields.io">
</p>

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

## 🎨 Оформление уведомлений (HTML Style)

Бот формирует структурированные отчеты. Благодаря **HTML parse mode**, администратор получает удобную карточку обращения.

<table width="100%">
<tr>
<td bgcolor="#1c1c1c">
<pre>
📩 <b>Новое обращение</b> от <a href="tg://user?id=12345">Пользователь</a>

📌 <b>Тема:</b> <code>Не работает кнопка</code>
📝 <b>Описание:</b> <i>При нажатии на "Оформить" страница перезагружается.</i>
</pre>
</td>
</tr>
</table>

*   **Жирный шрифт** (`<b>`): Акценты на заголовках.
*   **Инлайновая ссылка** (`<a>`): Переход в чат с пользователем в один клик.
*   **Моноширинный текст** (`<code>`): Тема обращения (удобно копировать).

---

## 🕒 Сценарий диалога (FSM)
Бот использует **Finite State Machine** для пошагового сбора данных:
1.  <b>Старт</b>: Приветствие и описание функций.
2.  <b>Причина</b>: Сбор краткой темы (Title).
3.  <b>Подробности</b>: Сбор детального описания (Description).
4.  <b>Финал</b>: Мгновенная отправка в админ-чат.

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
