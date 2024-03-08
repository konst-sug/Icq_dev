import logging
import json
import time
import random

from bot.bot import Bot
from bot.filter import Filter, MessageFilter
from bot.bot import BotButtonCommandHandler
from bot.bot import MessageHandler

from config import token, geopoints, geo, pictures
from keyboards import st_markup, cities_markup
from functions import get_react_icon, get_by_points, pretty_name

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y.%m.%d %I:%M:%S %p', level=logging.INFO)


bot = Bot(token=token)


def build_text(data, pict_id='0aO6S000XffeNUHBlceaqv65cf5ee61ae'):
    res_st = []
    for k,v in data.items():
        data = k
        temp, status = v[0], get_react_icon(v[1])
        dt = data.split('-')
        res_st.append(f'Дата {dt[2]}.{dt[1]}.{dt[0][2:]}г -Темп. {temp}C {status}\n')
    return ''.join(res_st)


def start_scr(bot,event):
    helo_msg = "Привет. Это погодный бот. Начнем?"
    bot.send_text(chat_id=event.from_chat, text=helo_msg, inline_keyboard_markup=json.dumps(st_markup))


def wea_scr(bot, event):
    chg_text = "Выбор города для погоды на 10 дней "
    bot.send_text(chat_id=event.from_chat, text=chg_text, inline_keyboard_markup=json.dumps(cities_markup))
    

def city1(bot,event):
    citi1_text = "Это прогноз погоды для Ленинграда на 7 дней"
    bot.send_text(chat_id=event.from_chat, text=citi1_text)
    data = get_by_points(geopoints[1]['latitude'], geopoints[1]['longitude'])
    bot.send_file(chat_id=event.from_chat, file_id='0aO6S000XffeNUHBlceaqv65cf5ee61ae',caption=build_text(data))
    time.sleep(1)   
    wea_scr(bot,event)


def city2(bot,event):
    citi1_text = "Это прогноз погоды для Москвы на 7 дней"
    bot.send_text(chat_id=event.from_chat, text=citi1_text)
    data = get_by_points(geopoints[0]['latitude'], geopoints[0]['longitude'])
    bot.send_file(chat_id=event.from_chat, file_id='0ak7K0005vt8mGOdUA99CR65cf5fbf1ae', caption=build_text(data))
    time.sleep(1)   
    wea_scr(bot,event)


def city3(bot,event):
    data = get_by_points(geopoints[2]['latitude'], geopoints[2]['longitude'])
    citi1_text = "Это прогноз погоды для Воронежа на 7 дней"
    bot.send_text(chat_id=event.from_chat, text=citi1_text)
    bot.send_file(chat_id=event.from_chat, file_id='0cU9G000d7hvhqKIljhm0a65cf60891ae', caption=build_text(data))
    time.sleep(1)   
    wea_scr(bot,event)


def city4(bot,event):
    citi1_text = "Это прогноз погоды для Берлина на 7 дней"
    data = get_by_points(geopoints[3]['latitude'], geopoints[3]['longitude'])
    bot.send_text(chat_id=event.from_chat, text=citi1_text)
    bot.send_file(chat_id=event.from_chat, file_id='0fuak000UQ8yBXjA8y3p6965cf60bc1ae', caption=build_text(data))
    time.sleep(1)   
    time.sleep(1)   
    wea_scr(bot,event)


def city5(bot,event):
    citi1_text = "Это прогноз погоды для Самары на 7 дней"
    data = get_by_points(geopoints[4]['latitude'], geopoints[4]['longitude'])
    bot.send_text(chat_id=event.from_chat, text=citi1_text)
    bot.send_file(chat_id=event.from_chat, file_id='0cU7K0001mAOpH8AhREM9P65cf603c1ae', caption=build_text(data))
    time.sleep(1)   
    wea_scr(bot,event)


def city6(bot,event):
    citi1_text = "Ввод города"
    bot.send_text(chat_id=event.from_chat, text=citi1_text)
    bot.send_file(chat_id=event.from_chat, file_id='0jmcV000Nfk9P3O3tVyPbJ65c36c841ae')
    input_city(bot,event)


def input_city(bot, event):    
    tip = event.data['text']
    try:
        if tip.lower() in geo.keys():
            lat = geo[tip.lower()][0]
            long = geo[tip.lower()][1]
            data = get_by_points(float(lat), float(long)) 
            bot.send_text(chat_id=event.from_chat, text=f"Это прогноз погоды для города {pretty_name(event.text)} на 7 дней")
            bot.send_file(chat_id=event.from_chat, file_id=random.choice(pictures), caption=build_text(data))
        else:
            bot.send_file(chat_id=event.from_chat, file_id='0cU7K0001mAOpH8AhREM9P65cf603c1ae', caption='Город не найден')    
    except Exception as error:
        print(f"Error in block inputcity + {error}")
    finally:
        time.sleep(5)   
        wea_scr(bot,event)


def main():
    bot.dispatcher.add_handler(MessageHandler(callback=start_scr))
    bot.dispatcher.add_handler(MessageHandler(callback=input_city))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=wea_scr, filters=Filter.callback_data("begin")))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=city1, filters=Filter.callback_data("btn1")))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=city2, filters=Filter.callback_data("btn2")))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=city3, filters=Filter.callback_data("btn3")))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=city4, filters=Filter.callback_data("btn4")))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=city5, filters=Filter.callback_data("btn5")))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=city6, filters=Filter.callback_data("btn6")))

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()