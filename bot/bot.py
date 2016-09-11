# coding: utf-8

import requests

import telebot
import config

bot = telebot.TeleBot(config.TOKEN_BOT)


@bot.message_handler(content_types=['text'])
def paste_code(message):
    params = {
        'api_dev_key': config.API_KEY,
        'api_option': config.API_OPTION,
        'api_paste_code': message.text
    }
    data = requests.post(config.PASTE_BIT_URL, params)
    bot.send_message(message.chat.id, data.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)