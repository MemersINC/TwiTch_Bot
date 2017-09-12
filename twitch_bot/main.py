import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")))

from twitch_bot.twitch import TChannel
import re
import requests
import json
from twitter import *
import random
import time

URL = "https://twitchemotes.com/api_cache/v3/global.json"
top_channels_url = "https://api.twitch.tv/kraken/streams/"
req = requests.get(top_channels_url, headers={"Client-ID": 'xd'})
wtf_is_this = json.loads(req.text)



token = xd
token_secret = xd
consumer_key = 'xd'
consumer_secret = 'xd'

t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

pattern = re.compile(r" :(.+)\\r\\n'")
pattern_words = re.compile(r"\w+")
request = requests.get(URL)
emotes_dict = json.loads(request.text)
emotes = list(emotes_dict.keys())
tweets = []


def on_message(obj, message):
    message = str(message)
    match = pattern.findall(message)
    if len(match) > 0 and len(match) < 140:
        words = pattern_words.findall(match[0])
        emote_count = 0
        normal_count = 0
        for word in words:
            if word in emotes:
                emote_count += 1
            else:
                normal_count += 1

        if emote_count > 1 and normal_count > 0:
            t.statuses.update(status=match[0])

def main():
    channels = []
    for thing in wtf_is_this['streams'][:20]:
        channels.append(thing['channel']['name'])
    channel = TChannel(on_message, channel=channels)
    channel.join()


if __name__ == "__main__":
    main()