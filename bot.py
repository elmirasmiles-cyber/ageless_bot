import os
from flask import Flask, request
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ===== Токен от BotFather =====
API_TOKEN = os.environ.get("МОЙ ТОКЕН")
bot = telebot.TeleBot(API_TOKEN, parse_mode="HTML")

# ===== ПОЛНЫЙ СПИСОК СТАТЕЙ =====
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
    "ПИТАНИЕ МОЛОДОСТИ": [
        ("Книжный анти-эйдж: «Кинечник и мозг» Дэвида Перлмуттера", "https://t.me/timeforselfcare/121"),
        ("Как правильно выбрать БАД", "https://t.me/timeforselfcare/142"),
        ("Коллаген - гид по главному белку молодости", "https://t.me/timeforselfcare/123"),
        ("Часть 2.Какой бывает и как выбрать", "https://t.me/timeforselfcare/124"),
        ("Часть 3. У кого не будет работать", "https://t.me/timeforselfcare/125"),
        ("Психобиотики: фабрика радости внутри вас", "https://t.me/timeforselfcare/73"),
        ("FMD - омоложение через обман голода", "https://t.me/timeforselfcare/74"),
        ("Железодефицитная анемия - как отловить вовремя", "https://t.me/timeforselfcare/75"),
        ("Anti-age в тарелке - я на очередном биохакерском форуме", "https://t.me/timeforselfcare/80"),
        ("Аутофагия - встроенный пылесос организма", "https://t.me/timeforselfcare/57"),
        ("Магний: гид по главному дзен-минералу", "https://t.me/timeforselfcare/65"),
        ("Мои топ-4 добавок, которые проверенно работают", "https://t.me/timeforselfcare/64"),
    ],
    "ЛИЦО БЕЗ КОСМЕТОЛОГОВ И ХИМИИ": [
        ("Искусство держать лицо - эффективно тормозим старение", "https://t.me/timeforselfcare/98"),
        ("Побочки косметологии в погоне за коллагеном", "https://t.me/timeforselfcare/130"),
        ("Что с лицом? Как косметологи почти угробили мое лицо", "https://t.me/timeforselfcare/133"),
        ("Что с лицом - 2: спасение откуда не ждали", "https://t.me/timeforselfcare/135"),
        ("Что вышло, то вышло - апдейт лица от Энджи", "https://t.me/timeforselfcare/137"),
        ("Методика Пратимы Райчур - всё о красоте кожи изнутри", "https://t.me/timeforselfcare/61"),
        ("Методика Нигмы Талиб- как еда влияет на кожу", "https://t.me/timeforselfcare/66"),
        ("Тест на тип кожи по методике Нигмы Талиб", "https://t.me/timeforselfcare/69"),
        ("Коллаген - гид по главному белку молодости. Часть 1.", "https://t.me/timeforselfcare/123"),
        ("Коллаген. Часть 2.Какой бывает и как выбрать", "https://t.me/timeforselfcare/124"),
        ("Коллаген. Часть 3. У кого не будет работать", "https://t.me/timeforselfcare/125"),
    ],
    "НАТУРАЛЬНЫЙ УХОД ЗА СОБОЙ": [
        ("Крик души, или ода дезодорантам", "https://t.me/timeforselfcare/88"),
        ("Глюки подмены: искусство маскировки проблем как стиль жизни", "https://t.me/timeforselfcare/47"),
        ("Мои топ-4 добавок, которые проверенно работают", "https://t.me/timeforselfcare/64"),
        ("Коллаген - гид по главному белку молодости", "https://t.me/timeforselfcare/123"),
        ("Как прозреть обратно - что я делаю, чтобы вернуть просевшее зрение", "https://t.me/timeforselfcare/91"),
        ("Как правильно выбрать БАД", "https://t.me/timeforselfcare/142"),
        ("Методика Пратимы Райчур - всё о красоте кожи изнутри", "https://t.me/timeforselfcare/61"),
        ("Методика Нигмы Талиб- как еда влияет на кожу", "https://t.me/timeforselfcare/66"),
        ("Тест на тип кожи по методике Нигмы Талиб", "https://t.me/timeforselfcare/69"),
        ("Магний: гид по главному дзен-минералу", "https://t.me/timeforselfcare/65"),
        ("Психобиотики: фабрика радости внутри вас", "https://t.me/timeforselfcare/73"),
    ],
    "МОТИВАТОРЫ": [
        ("Диктует ли возраст правила? Спросите Тома Круза и Джей Ло", "https://t.me/timeforselfcare/77"),
        ("Крик души, или ода дезодорантам", "https://t.me/timeforselfcare/88"),
        ("Биохимия счастья - как управлять своими состояниями", "https://t.me/timeforselfcare/93"),
        ("Мне 51", "https://t.me/timeforselfcare/145"),
        ("Йога как ресурс (который всегда с тобой)", "https://t.me/timeforselfcare/59"),
        ("Почему только сейчас: как нас тормозят наши убеждения", "https://t.me/timeforselfcare/62"),
        ("Йога, которая мурчит - как управлять своим состоянием", "https://t.me/timeforselfcare/68"),
    ],
    "БИОХАКИНГ НА ПРАКТИКЕ": [
        ("Обо мне и этом канале", "https://t.me/timeforselfcare/27"),
        ("Как правильно выбирать БАД", "https://t.me/timeforselfcare/142"),
        ("Мне 51", "https://t.me/timeforselfcare/145"),
        ("Здоровый человек, или \"чтобы что\"", "https://t.me/timeforselfcare/30"),
        ("Мои топ-4 добавок, которые проверенно работают", "https://t.me/timeforselfcare/64"),
        ("Магний: гид по главному дзен-минералу", "https://t.me/timeforselfcare/65"),
        ("Я на конференции \"Поколение вне возраста\"", "https://t.me/timeforselfcare/70"),
        ("Иллюзия тщетности - отрывок из моей книги", "https://t.me/timeforselfcare/41"),
        ("Что можно начать делать в 35+", "https://t.me/timeforselfcare/53"),
        ("Аутофагия - как работает встроенный пылесос организма", "https://t.me/timeforselfcare/57"),
        ("FMD - интенсивно омолаживающий лайфхак", "https://t.me/timeforselfcare/74"),
    ],
    "ПРИЧИНЫ СТАРЕНИЯ": [
        ("Почему тело разрушается - краткий гид по теориям", "https://t.me/timeforselfcare/32"),
        ("Теломерная теория старения", "https://t.me/timeforselfcare/36"),
        ("Теория свободнорадикального старения", "https://t.me/timeforselfcare/37"),
        ("Гормональная теория старения", "https://t.me/timeforselfcare/39"),
        ("Сахарное старение, или теория перекрестных сшивок", "https://t.me/timeforselfcare/50"),
    ],
    "ДАЙТЕ ВСЁ": [
        ("Все посты апреля", "https://t.me/timeforselfcare/56"),
        ("Все посты мая", "https://t.me/timeforselfcare/71"),
        ("Все посты июня", "https://t.me/timeforselfcare/103"),
        ("Все посты июля", "https://t.me/timeforselfcare/138"),
        ("Все посты августа", "https://t.me/timeforselfcare/138"),
    ],
}

# ===== Сокращенные названия категорий =====
CATEGORY_IDS = {category: f"cat{i}" for i, category in enumerate(articles.keys())}
ID_TO_CATEGORY = {v: k for k, v in CATEGORY_IDS.items()}

def truncate_text(text, max_length=64):
    return text if len(text) <= max_length else text[:max_length-3] + "..."

def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    for category in articles.keys():
        markup.add(InlineKeyboardButton(category, callback_data=CATEGORY_IDS[category]))
    return markup

def articles_menu(category_id):
    category_name = ID_TO_CATEGORY[category_id]
    markup = InlineKeyboardMarkup(row_width=1)
    for title, url in articles[category_name]:
        markup.add(InlineKeyboardButton(truncate_text(title), url=url))
    markup.add(InlineKeyboardButton("⬅️ Назад к категориям", callback_data="back"))
    return markup

# ===== Flask для webhook =====
app = Flask(__name__)

@app.route(f"/{API_TOKEN}", methods=["POST"])
def webhook():
    json_data = request.get_json()
    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def index():
    return "Бот работает!", 200

# ===== Обработчики команд =====
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "📚 **База anti-age наработок Эльмиры**\n\nВыберите раздел:",
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.startswith("cat"):
        if call.data in ID_TO_CATEGORY:
            category_name = ID_TO_CATEGORY[call.data]
            bot.edit_message_text(
                f"📖 **{category_name}**\n\nВыберите из списка:",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=articles_menu(call.data)
            )
        else:
            bot.answer_callback_query(call.id, "❌ Раздел не найден")
    elif call.data == "back":
        bot.edit_message_text(
            "📚 **База anti-age наработок Эльмиры**\n\nВыберите раздел:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )

# ===== Настройка webhook для Railway =====
bot.remove_webhook()
RAILWAY_URL = os.environ.get("RAILWAY_URL")  # вставь URL своего проекта в переменные окружения
bot.set_webhook(url=RAILWAY_URL + API_TOKEN)

# ===== Запуск Flask =====
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)