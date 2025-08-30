import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

# ===== Токен =====
API_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN, parse_mode="HTML")

# ===== СТАТЬИ =====
articles = {
    "ГОРМОНЫ И МОЛОДОСТЬ": [
        ("Гормоны стресса: цель, суть и последствия.", "https://t.me/timeforselfcare/116"),
        ("Часть 1. Адреналин и норадреналин", "https://t.me/timeforselfcare/117"),
        ("Часть 2. Кортизол", "https://t.me/timeforselfcare/118"),
        ("Гормональное расписание тела", "https://t.me/timeforselfcare/42"),
        ("Гормоны и переедание: 1. Причины", "https://t.me/timeforselfcare/148"),
        ("Гормоны и переедание: 2. Инсулин", "https://t.me/timeforselfcare/154"),
        ("Гормоны и переедание: 3. Гормоны голода и сытости", "https://t.me/timeforselfcare/157"),
        ("Гормоны и переедание: 4. Пептид PYY: стоп-датчик насыщения", "https://t.me/timeforselfcare/160"),
        ("Гормоны и переедание: 5. Кортизол - творец хаоса", "https://t.me/s/timeforselfcare/162"),
    ],
    "ANTI-AGE НАСТРОЙКИ УМА": [
        ("Ответы на ваши вопросы - как внедрить новые привычки", "https://t.me/timeforselfcare/106"),
        ("Тормоза в голове: Серия 1.Зачем?", "https://t.me/timeforselfcare/111"),
        ("Серия 2. Как хакнуть сопротивление мозга", "https://t.me/timeforselfcare/114"),
        ("Глюки подмены: маскировка проблем как стиль жизни", "https://t.me/timeforselfcare/47"),
        ("Книжный anti-age: \"Тонкое искусство пофигизма\"", "https://t.me/timeforselfcare/49"),
        ("Книжный anti-age: \"5 столпов богатства\"", "https://t.me/timeforselfcare/139"),
        ("Психобиотики: фабрика радости внутри вас", "https://t.me/timeforselfcare/73"),
        ("Биохимия счастья - как управлять своими состояниями", "https://t.me/timeforselfcare/93"),
    ],
    # ... добавь остальные категории как у тебя были
}

# ===== МЕНЮ =====
def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    for category in articles.keys():
        markup.add(InlineKeyboardButton(category, callback_data=f"cat_{category}"))
    return markup

def articles_menu(category):
    markup = InlineKeyboardMarkup(row_width=1)
    for title, url in articles[category]:
        short_title = title if len(title) <= 64 else title[:61] + "..."
        markup.add(InlineKeyboardButton(short_title, url=url))
    markup.add(InlineKeyboardButton("⬅️ Назад", callback_data="back"))
    return markup

# ===== КОМАНДЫ =====
@bot.message_handler(commands=["start"])
def start(message):
    hide_keyboard = ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Загружаем меню...", reply_markup=hide_keyboard)
    
    bot.send_message(
        message.chat.id,
        "📚 **База anti-age наработок Эльмиры**\n\nВыберите раздел:",
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.startswith("cat_"):
        category = call.data[4:]  # Убираем "cat_"
        if category in articles:
            bot.edit_message_text(
                f"📖 **{category}**\n\nВыберите статью:",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=articles_menu(category)
            )
    elif call.data == "back":
        bot.edit_message_text(
            "📚 **База anti-age наработок Эльмиры**\n\nВыберите раздел:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )

# ===== ЗАПУСК =====
if __name__ == "__main__":
    print("🟢 Бот запущен!")
    bot.infinity_polling()