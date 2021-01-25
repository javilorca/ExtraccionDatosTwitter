import tweepy
import json

# 4 cadenas para la autenticación
consumer_key = "0Ejo5ertaZNsMVlrRDci59Eez"
consumer_secret = "qyKXGADkjNxoWOveIZH2V1qg3HAU3n8qha2lk27zgeLAe8ktSO"
access_token = "294340163-iZZ83fdkMUfQIVuu7tTO4SOXXrQkrCA4xmr4DB3I"
acces_tokken_secret = "i02IvqMNt64gTDvI9MKvzCjZbf8i6f5su6giel7dVMOyk"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_tokken_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Publicar un tweet
#api.update_status("Pr1")


#Hacer un retwit
#ultimo_tweet_id = '338267984520949760'
#api.retweet(ultimo_tweet_id)

#data = api.me()
#json_data = json.dumps(data._json, indent=4)
#print (json_data)

#Sacar ID del último tweet y darle Like
data = api.me()
id_ultimo_tweet = data._json["status"]["id"]
@print(id_ultimo_tweet)

#Dar Liker último tweet
api.create_favorite(id_ultimo_tweet)

#Quitar Liker último tweet
#api.destroy_favorite(id_ultimo_tweet)

#Responder a un tweet
api.update_status("Pr2 x2",
                  in_replay_to_status_id=id_ultimo_tweet)