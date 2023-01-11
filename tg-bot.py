import telebot
from config import TOKEN
import random
from random import choice

bot = telebot.TeleBot(TOKEN)

def comrpes(messag):
    str = messag.text[0]
    bot.send_message(messag.chat.id, str)
    bot.send_sticker(messag.chat.id, 'CAACAgIAAxkBAAEG73Vjo1mRgC9-dIS5kUjjdMG09qeodAACXwEAAhAabSLLoLkqsC4-oywE')
    bot.send_message(messag.chat.id, 'Получите')

"""Команда Start"""
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Рандомное число до 100')
    item2 = telebot.types.KeyboardButton('Кинуть кубик')
    item3 = telebot.types.KeyboardButton('Да или Нет')
    item4 = telebot.types.KeyboardButton('Как дела?')
    item5 = telebot.types.KeyboardButton('Сжать')
    item6 = telebot.types.KeyboardButton('Знак зодиака')
    item7 = telebot.types.KeyboardButton('Угадайка')

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет, вот дела?')                                         
    elif message.text == 'Рандомное число до 100':
        bot.send_message(message.chat.id, str(random.randint(1, 100)))
    elif message.text == 'Да или Нет':
        answer = choice(['Да', 'Нет'])
        bot.send_message(message.chat.id, answer)
    elif message.text == 'Как дела?':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)

        item1 = telebot.types.InlineKeyboardButton('не очень', callback_data='1')
        item2 = telebot.types.InlineKeyboardButton('хорошо', callback_data='2')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Отлично, а у вас?', reply_markup=markup)

    elif message.text == 'Знак зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=3)

        item1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')
        item2 = telebot.types.InlineKeyboardButton('Телец', callback_data='Телец')
        item3 = telebot.types.InlineKeyboardButton('Близнец', callback_data='Близнец')
        item4 = telebot.types.InlineKeyboardButton('Рак', callback_data='Рак')
        item5 = telebot.types.InlineKeyboardButton('Лев', callback_data='Лев')
        item6 = telebot.types.InlineKeyboardButton('Дева', callback_data='Дева')
        item7 = telebot.types.InlineKeyboardButton('Весы', callback_data='Весы')
        item8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='Скорпион')
        item9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='Стрелец')
        item10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='Козерог')
        item11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='Водолей')
        item12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='Рыбы')        

        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

        bot.send_message(message.chat.id, 'Выберете свой знак', reply_markup=markup)    

    elif message.text == 'Кинуть кубик':
        bot.send_message(message.chat.id, f'Вам выпало {(random.randint(1, 6))}')
    elif message.text == 'Сжать':
        mesg = bot.send_message(message.chat.id, 'Введите строку которую хотите сжать')
        bot.register_next_step_handler(mesg, comrpes)    
    else:
        bot.send_message(message.chat.id, 'Данный функционал находится в разработке, таких команд пока не знаю. Лучше кликните на команду /start')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    dikt_znak = znak_har()
    if call.data == '1':
        bot.send_message(call.message.chat.id, 'Почему?')
    elif call.data == '2':
        bot.send_message(call.message.chat.id, 'Я рад')
    elif call.data == 'Овен':
        bot.send_message(call.message.chat.id, dikt_znak["Овен"])
    elif call.data == 'Телец':
        bot.send_message(call.message.chat.id, dikt_znak["Телец"])    
    elif call.data == 'Близнец':
        bot.send_message(call.message.chat.id, dikt_znak["Близнец"])
    elif call.data == 'Рак':
        bot.send_message(call.message.chat.id, dikt_znak["Рак"])                
    elif call.data == 'Лев':
        bot.send_message(call.message.chat.id, dikt_znak["Лев"])
    elif call.data == 'Дева':
        bot.send_message(call.message.chat.id, dikt_znak["Дева"])
    elif call.data == 'Весы':
        bot.send_message(call.message.chat.id, dikt_znak["Весы"])
    elif call.data == 'Скорпион':
        bot.send_message(call.message.chat.id, dikt_znak["Скорпион"])
    elif call.data == 'Стрелец':
        bot.send_message(call.message.chat.id, dikt_znak["Стрелец"])
    elif call.data == 'Козерог':
        bot.send_message(call.message.chat.id, dikt_znak["Козерог"])
    elif call.data == 'Водолей':
        bot.send_message(call.message.chat.id, dikt_znak["Водолей"])
    elif call.data == 'Рыбы':
        bot.send_message(call.message.chat.id, dikt_znak["Рыбы"])                            

def znak_har():
    dict = {}
    with open ('text.txt', 'r', encoding='utf-8') as file:
        for i in range(12):
            str1 = file.readline().split(' ', 1)
            dict[str1[0]] = str1[1]
        return dict    
bot.polling(none_stop=True)




