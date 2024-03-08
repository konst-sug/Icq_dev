import requests
import json
from requests.sessions import Session
from config import url_weather, url4, params




def sav_wea_data(url: str) -> None:
     s = requests.Session()

     req = s.get(url=url)
     with open('data.json', 'w') as file:
          json.dump(req.json(), file, indent=4, ensure_ascii=False)
         
     #открываем файл на чтение    
     with open('data.json', 'r', encoding='utf-8') as fh: 
     #загружаем из файла данные в словарь data
          data = json.load(fh) 
     print(data["daily"])


def get_data_list(url: str) -> dict:
     
     s = requests.get(url=url)
     data = s.json()
     wea_dict,i = {},0
     while i < 7:
          wea_dict[data["daily"]["time"][i]] = [data["daily"]["temperature_2m_max"][i], data["daily"]["weather_code"][i]]
          i += 1
    #  print(*wea_dict.items())
     return wea_dict



def get_by_points(lat: float, lon: float) -> dict:
     url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weather_code,temperature_2m_max&timezone=Europe%2FMoscow"
     s = requests.get(url=url)
     data = s.json()
     res_dict,i = {},0
     while i < 7:
          res_dict[data["daily"]["time"][i]] = [data["daily"]["temperature_2m_max"][i], data["daily"]["weather_code"][i]]
          i += 1
    # print(*res_dict.items())
    #  print(res_dict['2024-02-20'][0])
     return res_dict


def get_react_icon(code: int) -> str:
     """Преобразование кода погоды в иконку для вывода"""
     if code <= 1:
          icon = '☀️'
     elif 2 <= code <=  55:
          icon = '⛅️'
     elif 56 <= code <= 70: 
          icon = '🌧'
     elif  70 < code <= 79:
          icon = '❄️'
     elif  79 < code <= 86:
          icon = '🌨'
     else: 
          icon = '⛈'
     return icon    


def pretty_name(name: str) -> str:
     pr_name = f"{name[:1].capitalize()}{name[1:].lower()}"
     return pr_name


def main():
    #get_wea_data(url=url8)
    #get_data_list(url=url4)
    #get_by_points(53.20, 50.15)
   pass


if __name__ == "__main__":
    main()    