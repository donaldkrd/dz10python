import telebot
from config import TOKEN
import random
from random import choice
bot = telebot.TeleBot(TOKEN)

"""Команда СТАРТ"""
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Рандомное число до 100')
    item2 = telebot.types.KeyboardButton('Кинуть кубик')
    item3 = telebot.types.KeyboardButton('Да или Нет')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет, как дела?')
    elif message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, как дела?')
    elif message.text == 'Хорошо':
        bot.send_message(message.chat.id, 'Ты везучий человек, посмотри мой функционал нажав на /start')
    elif message.text == 'хорошо':
        bot.send_message(message.chat.id, 'Ты везучий человек, посмотри мой функционал нажав на /start')
    elif message.text == 'Нормально':
        bot.send_message(message.chat.id, 'Ты везучий человек, посмотри мой функционал нажав на /start')
    elif message.text == 'нормально':
        bot.send_message(message.chat.id, 'Ты везучий человек, посмотри мой функционал нажав на /start')
    elif message.text == 'норм':
        bot.send_message(message.chat.id, 'Ты везучий человек, посмотри мой функционал нажав на /start')
    elif message.text == 'Норм':
        bot.send_message(message.chat.id, 'Ты везучий человек, посмотри мой функционал нажав на /start')
    elif message.text == 'Плохо':
        bot.send_message(message.chat.id, 'Понимаю, такое время. Посмотри мой функционал нажав на /start')
    elif message.text == 'плохо':
        bot.send_message(message.chat.id, 'Понимаю, такое время. Посмотри мой функционал нажав на /start')                                            
    elif message.text == 'Рандомное число до 100':
        bot.send_message(message.chat.id, str(random.randint(1, 100)))
    elif message.text == 'Да или Нет':
        answer = choice(['Да', 'Нет'])
        bot.send_message(message.chat.id, answer)         
    elif message.text == 'Кинуть кость':
        bot.send_message(message.chat.id, f'Вам выпало {(random.randint(1, 6))}')
    else:
        bot.send_message(message.chat.id, 'Данный функционал находится в разработке, таких команд пока не знаю. Лучше кликните на команду /start')

bot.polling(none_stop=True)









# import telebot
# from config import TOKEN

# bot = telebot.TeleBot(TOKEN)

# """Команда Старт"""
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id, 'Добрых вечеров, бродяги')

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text == 'привет':
#         bot.send_message(message.chat.id, 'Привет, как дела?')
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю, понимаю только слово "привет"')

# bot.polling(none_stop=True)
