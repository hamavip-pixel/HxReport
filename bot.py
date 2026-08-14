import os
import telebot

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سڵاو! من بۆتی HxReport مە، چۆن دەتوانم یارمەتیت بدەم؟ 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "سوپاس بۆ نامەکەت! نامەکەت گەیشت.")

if __name__ == '__main__':
    bot.infinity_polling()
