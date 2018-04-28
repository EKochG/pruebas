from datetime import datetime
import time
import tweepy
import random
from tweepy import *
consumer_key="VrrWb0wDoG2YvkVOXY0krIdP1"
consumer_secret="LINi3AaqDBYD4OeYPV752WuKMMgPMSo1evUhOu0afQwjdaK5tL"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
access_token="976231636642779137-3usy7F6Misxicy7WLQA3wbUJckWtjEb"
access_token_secret="n5QG8GnHdWGNRCVNGTc8JSlqePbmi3dBuumhpWjknBKYG"
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#api.update_status("holi")
#a!="20:34"
Dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
cont=5
elem=0
felicidades=["excelente","maginifico","genial","bacan","maravilloso"]
a=str(time.strftime("%H:%M")) 
while(True):
	if(a=="08:00"):
		elem=random.randrange(5)
		api.update_status("Hola a todos, espero que tengan un "+felicidades[elem]+" dia "+Dias_semana[cont])
	if(a=="13:00"):
		api.update_status("Hora de almuerzo, saludos!!")
	if(a=="21:00"):
		api.update_status("Hola, espero que todos hayan tenido un excelente dia"+Dias_semana[cont])
		cont=(cont+1)%7
	time.sleep(1)
	a=str(time.strftime("%H:%M")) 
	print(a)