import logging
import json

from bot.bot import Bot
from bot.filter import Filter
from bot.bot import BotButtonCommandHandler
from bot.bot import MessageHandler

from config import token
from keyboards import st_markup, cities_markup

logging.basicConfig(format=logging.BASIC_FORMAT)

bot = Bot(token=token)



def start_scr(bot,event):
    helo_msg = "Привет. Это погодный бот. Начнем?"
    bot.send_text(chat_id=event.from_chat, text=helo_msg, inline_keyboard_markup=json.dumps(st_markup))


def wea_scr(bot, event):
    chg_text = "Выбор города для погоды на 10 дней "
    bot.send_text(chat_id=event.from_chat, text=chg_text, inline_keyboard_markup=json.dumps(cities_markup))


def city1(bot,event):
    citi1_text = "Это прогноз погоды для города на 10 дней"
    bot.send_text(chat_id=event.from_chat, text=citi1_text)











def main():
    bot.dispatcher.add_handler(MessageHandler(callback=start_scr))
  
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=wea_scr, filters=Filter.callback_data("begin")))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=city1, filters=Filter.callback_data("piter")))

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()