#!/usr/bin/env python
import sys
from twython import Twython

tweetStr= "This is a test. I will announce here when I am a jerk. Gow."

CONSUMER_KEY = 'vVreZvEsEi2NWRpo6YBUkxmEa'
CONSUMER_SECRET = 'aMeHO8u04qA2LJfVD9nvriCmE3qgAIkETHxvUVLkuIIaYXgwWj'
ACCESS_KEY = '733902027294543873-dwNZKlt5nh5Ya8hOM2t8qmH5UlbvGcL'
ACCESS_SECRET = '7ceN0vPQJDwNJWDWX2fXbzP4gV8wVHpXDCwODHUsmEDy6'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=tweetStr)

print "Tweeted:" +tweetStr