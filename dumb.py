import tweepy
import json

# 4 cadenas para la autenticación
consumer_key = "0Ejo5ertaZNsMVlrRDci59Eez"
consumer_secret = "qyKXGADkjNxoWOveIZH2V1qg3HAU3n8qha2lk27zgeLAe8ktSO"
access_token = "294340163-iZZ83fdkMUfQIVuu7tTO4SOXXrQkrCA4xmr4DB3I"
acces_tokken_secret = "i02IvqMNt64gTDvI9MKvzCjZbf8i6f5su6giel7dVMOyk"

auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_tokken_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Obtener información
#data = api.me()
#print json.dumps(data._json, indent=2)

#Obtener informacion de otro usuario
#data = api.get_user("nike")
#print json.dumps(data._json, indent=2)

#Obtener followers de un usuario
#data = api.followers(screen_name = "nike")
#print len(data)
#for user in data:
    #print json.dumps(user._json, indent=2)

#Obtener friends/followes de un usuario utilizando Cursor
#for user in tweepy.Cursor(api.friends, screen_name="nike").items(100):
    #print(json.dumps(user._json,indent=2))


#Obtener un timeline
#for tweet in tweepy.Cursor(api.user_timeline, screen_name="puri_0210", tweet_mode="extended").items(1):
    #print(json.dumps(tweet._json, indent=2))


#Buscar tweet
for tweet in tweepy.Cursor(api.search, q="covid", tweet_mode="extended").items(10):
    print(json.dumps(tweet._json, indent=2))