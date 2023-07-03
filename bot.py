from telebot import types
from aiogram import types, Dispatcher, Bot
import telebot
from telebot import types
from django.core.management.base import BaseCommand
from .ainek.models import RSSSubs

TOKEN = '6269923322:AAFZCKucj1Uv9llwkNP9ijfao6b6LDTJFJo'

bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=["start"])
def start(message: types.Message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1 = types.KeyboardButton('Отдел')
  item2 = types.KeyboardButton('Акционные товары')
  item3 = types.KeyboardButton('Вакансии')
  item4 = types.KeyboardButton('Прайс лист')


  markup.add(item1, item2, item3, item4 )

  bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}! Вас приветсвует компания AinecStorу производство'.format(message.from_user), reply_markup = markup )


@bot.message_handler(content_types=['text'])
def bot_message(message):
  if message.chat.type == 'numer order':
    if message.text == 'в прцессе ':
      bot.send_message(message.chat.id, 'Ваш номер заказа: '+str())

def send_message_to_all_users_by_telegram(message: str, users: list):
    users_queryset = RSSSubs.objects.filter(id__in=users)
    for user in users_queryset:
        bot.send_message(user.telegram_id, message)

if __name__ == '__main__':
    bot.polling(non_stop=True)