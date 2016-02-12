# -*- coding: utf-8-*-
import random
import re
import wolframalpha
import time
import sys
from sys import maxint
from jasper import plugin

class WolframAlphaPlugin(plugin.SpeechHandlerPlugin):
	def get_phrases(self):
        	return ["WHO","WHAT","HOW MUCH", "HOW MANY", "HOW OLD"]

	def handle(self, text, mic):
	    app_id = self.profile['keys']['WOLFRAMALPHA']
	    client = wolframalpha.Client(app_id)

	    query = client.query(text)
	    if len(query.pods) > 0:
		texts = ""
		pod = query.pods[1]
		if pod.text:
		    texts = pod.text
		else:
		    texts = "I can not find anything"

		mic.say(texts.replace("|",""))
	    else:
		mic.say("Sorry, Could you be more specific?.")

	def is_valid(self, text):
	    return any(p.lower() in text.lower() for p in self.get_phrases())
