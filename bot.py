import tweepy
import constants
import requests
import logging

#Recibir mensajes de exito o error del bot
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

#Crear el cliente 

client = tweepy.Client(
    consumer_key = constants.CONSUMER_KEY,
    consumer_secret = constants.CONSUMER_SECRET,
    access_token = constants.ACCESS_TOKEN,
    access_token_secret = constants.ACCESS_TOKEN_SECRET
    )



tweet_text = "Hello, Twitter"
client.create_tweet(text= tweet_text)