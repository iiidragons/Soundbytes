import requests
import random

def vocalize(text, voice="random"):
    API_KEY = "0fca8d1bdf3c4dc1bf3e1fc03a5c0f83"
    voices = ["linda", "amy", "mary", "john", "mike"]
    if voice == "random":
        voice = random.choice(voices)
    elif voice == "musk":
        voice = "mike"
    elif voice == "freeman":
        voice = "john"
    elif voice == "male":
        voice = "mike"
    elif voice == "female":
        voice = "mary"
    url = "https://api.voicerss.org/?key={}&hl=en-us&b64=true&v={}&src={}".format(API_KEY, voice, text)
    response = requests.get(url)
    return response.content