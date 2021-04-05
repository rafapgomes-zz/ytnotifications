import ttkeys
import tweepy
autenticacao = tweepy.OAuthHandler(ttkeys.consumer_key,ttkeys.consumer_secret)

autenticacao.set_access_token(ttkeys.access_token,ttkeys.access_token_secret)

twitter = tweepy.API(autenticacao)

def posttweet(text):
    twitter.update_status(text)



def searchownTL(id):
    return twitter.user_timeline(userid=id,tweet_mode="extended")

def getvideourl(timeline):
    vetor =[]
    for tweet in timeline:
       vetor.append(tweet.entities['urls'][0]['expanded_url'])
    return vetor

def splitvetor(vet):
    split = []
    for i in vet:
       split.append(i[32:43])
    return split




