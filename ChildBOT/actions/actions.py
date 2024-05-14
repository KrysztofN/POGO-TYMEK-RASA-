from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, Restarted
from .date_check import get_date
from .calc_diff import calc_dif
import datetime
import requests


class ActionWeatherNow(Action):

    def name(self) -> Text:
        return "action_tell_weather"

    def run(self, dispatcher, tracker, domain):

            loc = tracker.get_slot('GPE')
            date = tracker.get_slot('Date')


            date = get_date(date)
            if date is None:
                dispatcher.utter_message(text="To nie jest poprawny format daty.")
                return [SlotSet("Date", None), FollowupAction("utter_date")]

            degree_sign = u'\N{DEGREE SIGN}'
            api_key = 'a24e1746e81fbe3720efe9962684d6d5'
            payload = {'q': loc, 'units': 'metric', 'appid': api_key, 'lang': 'pl'}
            response = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=payload)

            try:
                data = response.json()
                cur_date = datetime.datetime.now()
                cur_date_o = datetime.datetime(cur_date.year, cur_date.month, cur_date.day)
                timestamp1 = cur_date_o.timestamp()
                timestamp2 = date.timestamp()
                num = calc_dif(timestamp1, timestamp2)

                if num < 0 or num > 5:
                    dispatcher.utter_message(text="Nie jestem w stanie podać pogody na wskazaną datę. Przewiduję pogodę jedynie na 6 dni od dzisiejszej daty!")
                    return [SlotSet("Date", None), FollowupAction("utter_date")]
                else:
                    specific_date = datetime.datetime.now() + datetime.timedelta(days=num)
                    city = data['city']['name']
                    desc = None
                    temp = None
                    humidity = None
                    wind_speed = None
                    clouds = None

                    for item in data['list']:
                        date = datetime.datetime.utcfromtimestamp(item['dt'])
                        if date.date() == specific_date.date():
                            temp = item['main']['temp']
                            desc = item['weather'][0]['description']
                            humidity = item['main']['humidity']
                            wind_speed = item['wind']['speed']
                            clouds = item['clouds']['all']
                            break

                    weather_data = """
                                        Pogoda na ({}) w {}: \n {}{}C. {} , wilgotność powietrza na poziomie {}%. Prędkość wiatru {} m/s. Zachmurzenie {}%.""".format(
                        specific_date.strftime("%d-%m-%Y"), city, temp, degree_sign, desc, humidity, wind_speed, clouds)
                    dispatcher.utter_message(weather_data)
                    return [SlotSet("GPE", None), SlotSet("Date", None)]

            except (Exception, requests.exceptions.HTTPError) as e:
                dispatcher.utter_message(text="Nie udało się znaleźć miasta! Sprawdź pisownię")
                return [SlotSet("GPE", None), FollowupAction("utter_loc")]


class ActionRestartConversation(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

class ActionSetExecutedTrue(Action):

    def name(self) -> str:
        return "action_set_executed_true"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("terms", True)]
