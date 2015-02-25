# -*- coding: utf-8-*-
import random
import re
import wolframalpha
import time
import sys
from client import jasperpath
WORDS = ["SEARCH"]
PRIORITY = 1


def handle(text, mic, profile):
    messages=["What would you like know?",
        " what are you looking for?"]
    messages=random.choice(messages)
    mic.say(messages)
    question(mic.activeListen(),mic,profile)


def question(text,mic,profile):

    app_id=profile['keys']['WOLFRAMALPHA']
    client = wolframalpha.Client(app_id)

    query = client.query(text)

    if len(query.pods) > 0:
        texts = ""
        pod = res.pods[1]
        if pod.text:
            texts = pod.text
        else:
            texts = "I can not find anything"

        mic.say(texts.replace("|",""))
    else:
        mic.say("Sorry, Could you be more specific?.")

def isValid(text):
    return bool(re.search(r'\bsearch\b', text, re.IGNORECASE))
