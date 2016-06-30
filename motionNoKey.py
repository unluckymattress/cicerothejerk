from gpiozero import MotionSensor
import time
import math
import random
from twython import Twython

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

# Tweets sent out
tweet1 = "OM NOM NOM NOM"
tweet2 = "I tried to eat a clock. It was very time consuming."
tweet3 = "I decided that becoming a vegetarian was a missed steak."
tweet4 = "Lunch brought to you by Purr-rina."
tweet5 = "Don't go bacon my heart."
tweet6 = "You're a real pizza work!"

# set tweets to an array
tweetBank = [tweet1, tweet2, tweet3, tweet4, tweet5, tweet6]

# randomly select a tweet
randTweet = random.choice(tweetBank)

# sense motion 
pir = MotionSensor(4)
# loop until detecting motion
while True:
    if pir.motion_detected:
        print("Motion detected!")
        # send tweet
        api.update_status(status=randTweet)
        print "Tweeted:" + randTweet
        # sleep for 10 mins
	time.sleep(600.00)
    else:
	print("No motion")
	time.sleep(1)

            

