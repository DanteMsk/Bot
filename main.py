import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.first_name}!</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode="html")


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = f"<b>ты сказал:  {message.text}</b>"
    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)
