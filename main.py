import url
import telebot
import sqlite3
from config import token

with sqlite3.connect('database.db') as db:
    data = db.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS users(
        login TEXT, 
        password TEXT,
        id_telegram TEXT

)
    """
    data.executescript(table)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Пожалуйста, введи логин, предоставленные наставником, чтобы получить доступ к сайту. /authorization")

@bot.message_handler(commands=['authorization'])
def authorization(mess):
    bot.send_message("Введи логин: ")
    @bot.message_handler(content_types=["text"])
    def login_auth(message):
        bot.reply_to(message, f"Ваша ссылка {url}/auto_auth?login=<{message}>&hashed_password=<123123>")
bot.infinity_polling()