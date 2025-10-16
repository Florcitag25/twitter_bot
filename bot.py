import tweepy
import constants
import requests
import logging
from apscheduler.schedulers.blocking import BlockingScheduler

#Recibir mensajes de exito o error del bot
""" logging.basicConfig(level=logging.INFO, filename='bot.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s') """

#Crear el cliente 
def create_client(consumer_key, consumer_secret,access_token,access_token_secret):
    client = tweepy.Client(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret
        )
    return client

#Obtener clima de la API de Openweathermap
def get_weather(weather_api_key,city,country):
    weather_r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={weather_api_key}&units=metric")
    weather_data = weather_r.json()
    temp = weather_data["main"]["temp"]
    return temp

def create_tweet(client,text):
    client.create_tweet(text=text)

#Valor de la Key para API clima
weather_key = constants.WEATHER_API_KEY


client = create_client(constants.CONSUMER_KEY,constants.CONSUMER_SECRET,constants.ACCESS_TOKEN,constants.ACCESS_TOKEN_SECRET)
temp = str(get_weather(weather_key,"Salta","AR"))
scheduler = BlockingScheduler()
scheduler.add_job(create_tweet,"interval",hours=1,args=[client,temp])
scheduler.start()

