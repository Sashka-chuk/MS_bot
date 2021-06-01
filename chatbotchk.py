import telebot
from telebot import types

bot = telebot.TeleBot("1601411828:AAHt0Lo-U_owRiuEpsW0_thJBGtMVh_6X08")

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row("Привет", "Пока")


def send_welcome(id, text):
    bot.send_message(id, text, reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def answer(message):
    bot.send_message(message.chat.id, "Привет🤝")


@bot.message_handler(content_types=["text"])
def main(message):
    id = message.chat.id
    msg = message.text
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти", url="https://vk.com/sashkachyk")
    keyboard.add(url_button)
    if msg == 'Привет':
        bot.send_message(message.chat.id, "Привет, Нажмите на кнопку и перейди к моему создателю.", reply_markup=keyboard)
        bot.send_message(id, "Не забудьте поставить лайк на аватарку.")
    elif msg == 'Пока':
        bot.send_message(id, 'Ладно, пока✋.')
    elif msg == 'Почему':
        bot.send_message(id, 'Потому🥺')
    else:
        bot.send_message(id, 'Я вас не понимаю.')


bot.polling(none_stop=True)
