import telebot
from telebot import types  # для указание типов
import config
from config import quyuq,suyuq
import random
bot = telebot.TeleBot(config.token)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("suyuq")
    btn2 = types.KeyboardButton("quyuq")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Salom, {0.first_name}! hush kebsiz".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "suyuq"):
        bot.send_message(message.chat.id, text="Quyuq ovqat iching maslahatim :)")
    elif (message.text == "quyuq"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("qizil")
        btn2 = types.KeyboardButton("yashil")
        back = types.KeyboardButton("ortga")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="ranglardan birini tanlang", reply_markup=markup)

    elif (message.text == "qizil"):
        bot.send_message(message.chat.id,random.choice(suyuq))

    elif message.text == "yashil":
        bot.send_message(message.chat.id,random.choice(quyuq))

    elif (message.text == "ortga"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("suyuq")
        button2 = types.KeyboardButton("quyuq")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="bosh menyu", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="ERROR 404: WORD NOT FOUND ")


bot.polling(none_stop=True)