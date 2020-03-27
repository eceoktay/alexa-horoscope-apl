import logging
from flask import Flask
from flask_ask import Ask, statement, context
import json
import requests
import os

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

ASK_APPLICATION_ID = 'amzn1.ask.skill.2601967d-8c3f-4025-9dc9-3a3dd5bef850'

@ask.intent("horoscope_aries")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(0)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 0)

@ask.intent("horoscope_taurus")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(1)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 1)

@ask.intent("horoscope_gemini")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(2)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 2)

@ask.intent("horoscope_cancer")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(3)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 3)

@ask.intent("horoscope_leo")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(4)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 4)

@ask.intent("horoscope_virgo")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(5)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 5)

@ask.intent("horoscope_libra")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(6)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 6)

@ask.intent("horoscope_scorpio")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(7)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 7)

@ask.intent("horoscope_sagittarius")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(8)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 8)

@ask.intent("horoscope_capricorn")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(9)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 9)

@ask.intent("horoscope_aquarius")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(10)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 10)

@ask.intent("horoscope_pisces")
def main_function():
    if isDeviceSupportAPL() == False:
        return horoscopeTime(11)
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPL(data["document"], data["dataSources"], 11)

@ask.intent("AMAZON.StopIntent")
def stop_function():
    return statement("See you next time")

@ask.intent("AMAZON.CancelIntent")
def cancel_function():
    return statement("See you next time")

@ask.launch
def launched():
    if isDeviceSupportAPL() == False:
        return horoscopeTimeNoSign()
    with open('apl_template_export.json', 'r') as file:
        data = json.load(file)
        return horoscopeTimeAPLNoSign(data["document"], data["dataSources"])

@ask.session_ended
def session_ended():
    return "{}", 200

def isDeviceSupportAPL():
    interfaces = context.System.device.supportedInterfaces
    interfaces = str(interfaces)
    if "Alexa.Presentation.APL" in interfaces: 
        return True
    return False


horoscope_urls = (
    "http://horoscope-api.herokuapp.com/horoscope/today/",
    "http://horoscope-api.herokuapp.com/horoscope/week/",
    "http://horoscope-api.herokuapp.com/horoscope/month/"
)

sunsign_list = (
    "Aries", 
    "Taurus",
    "Gemini", 
    "Cancer", 
    "Leo", 
    "Virgo", 
    "Libra",  
    "Scorpio", 
    "Sagittarius", 
    "Capricorn",
    "Aquarius", 
    "Pisces"
)

sunsign_dates_list = (
    "(Mar.21 - Apr.19)", 
    "(Apr.20 - May 20)",
    "(May 21 - Jun.20)", 
    "(Jun.21 - Jul.22)", 
    "(Jul.23 - Aug.22)", 
    "(Aug.23 - Sep.22)", 
    "(Sep.23 - Oct.22)",  
    "(Oct.23 - Nov.21)", 
    "(Nov.22 - Dec.21)", 
    "(Dec.22 - Jan.19)",
    "(Jan.20 - Feb.18)", 
    "(Feb.19 - Mar.20)",
)

sunsign_image_list = (
    "https://www.dropbox.com/s/zfx5fvv7jh9xgcy/Aries.png?raw=1", 
    "https://www.dropbox.com/s/hbxzq056yem1r1w/Taurus.png?raw=1",
    "https://www.dropbox.com/s/sft4t8jobhvmqby/Gemini.png?raw=1", 
    "https://www.dropbox.com/s/8ui15dbmp51l5kg/Cancer.png?raw=1", 
    "https://www.dropbox.com/s/u1cgukflsls1q6e/Leo.png?raw=1", 
    "https://www.dropbox.com/s/2dskyjprm7sdj3y/Virgo.png?raw=1", 
    "https://www.dropbox.com/s/2vdj8qc6wbke13f/Libra.png?raw=1",  
    "https://www.dropbox.com/s/8mu2z459257ju46/Scorpio.png?raw=1", 
    "https://www.dropbox.com/s/b9c46xue447lwq7/Sagittarius.png?raw=1", 
    "https://www.dropbox.com/s/vfhpbycw1jos4k5/Capricorn.png?raw=1",
    "https://www.dropbox.com/s/hhi0wnh7j4lyy06/Aquarius.png?raw=1", 
    "https://www.dropbox.com/s/5z4k9za1xxl9g1n/Pisces.png?raw=1"
)

horoscope_detail_list = []

def getSunSign(index):
    return sunsign_list[index]

def getSunSignDates(index):
    return sunsign_dates_list[index]

def getSunSignImage(index):
    return sunsign_image_list[index]

def getHoroscopeDetail(index):
    return horoscope_detail_list[index]

def updateDataSources(dataSources, index):
    dataSources = json.dumps(dataSources)
    dataSources = dataSources.replace("[SUNSIGN_TEXT]", getSunSign(index))
    dataSources = dataSources.replace("[SUNSIGN_DATES_TEXT]", getSunSignDates(index))
    dataSources = dataSources.replace("[SUNSIGN_IMAGE]", getSunSignImage(index))
    dataSources = dataSources.replace("[DAILY_HOROSCOPE]", getHoroscopeDetail(0))
    dataSources = dataSources.replace("[WEEKLY_HOROSCOPE]", getHoroscopeDetail(1))
    dataSources = dataSources.replace("[MONTHLY_HOROSCOPE]", getHoroscopeDetail(2))
    dataSources = json.loads(dataSources, strict=False)
    return dataSources

def getHoroscope(index):
    horoscope_detail_list.clear()
    for i in range(0, len(horoscope_urls)):
        horoscope_url = horoscope_urls[i] + getSunSign(index)
        response = requests.get(horoscope_url)
        jsonValue = json.loads(response.text)
        if jsonValue["horoscope"][0] == '[':
            horoscope_detail_list.append(jsonValue["horoscope"][2:-2])
        else:
            horoscope_detail_list.append(jsonValue["horoscope"])

def getHoroscopeDetailsText(index):
    all_horoscope_text = ""
    for i in range(0, len(horoscope_detail_list)):
        if i == 0:
            all_horoscope_text = all_horoscope_text + getSunSign(index) + " Daily Horoscope: " + getHoroscopeDetail(0) + " "
        elif i == 1:
            all_horoscope_text = all_horoscope_text + getSunSign(index) + " Weekly Horoscope: " + getHoroscopeDetail(1) + " "
        elif i == 2:
            all_horoscope_text = all_horoscope_text + getSunSign(index) + " Monthly Horoscope: " + getHoroscopeDetail(2) + " "
    return all_horoscope_text

def horoscopeTime(index):
    getHoroscope(index)
    text = "Your horoscope: " + getHoroscopeDetailsText(index)
    jj = {
    "version": "1.0",
    "response": {
        "outputSpeech": {
            "type": "SSML",
            "ssml": "<speak>"+text+"</speak>"
        },
        'card': {
            'type': 'Simple',
            'title': "Horoscope Time",
            'content': text
        },
        "directives": [
        ],
        "shouldEndSession": True
    },
    "sessionAttributes": {},
    "userAgent": "ask-nodejs/1.0.25 Node/v6.10.3"
    }
    print(json.dumps(jj))
    return app.response_class(json.dumps(jj), content_type='application/json')

def horoscopeTimeAPL(document, dataSources, index):
    getHoroscope(index)
    dataSources = updateDataSources(dataSources, index)
    text = "Your horoscope: " + getHoroscopeDetailsText(index)
    jj = {
    "version": "1.0",
    "response": {
        "outputSpeech": {
            "type": "SSML",
            "ssml": "<speak>"+text+"</speak>"
        },
        'card': {
            'type': 'Simple',
            'title': "Horoscope Time",
            'content': text
        },
        "directives": [
            {
                "type": "Alexa.Presentation.APL.RenderDocument",
                "document": document,
                "datasources": dataSources,
                "token": "token"
            }
        ],
        "shouldEndSession": True
    },
    "sessionAttributes": {},
    "userAgent": "ask-nodejs/1.0.25 Node/v6.10.3"
    }
    print(json.dumps(jj))
    return app.response_class(json.dumps(jj), content_type='application/json')

def horoscopeTimeNoSign():
    text = "Please try, Alexa, ask horoscope time to give horoscope for leo"
    jj = {
    "version": "1.0",
    "response": {
        "outputSpeech": {
            "type": "SSML",
            "ssml": "<speak>"+text+"</speak>"
        },
        'card': {
            'type': 'Simple',
            'title': "Horoscope Time",
            'content': text
        },
        "directives": [
        ],
        "shouldEndSession": True
    },
    "sessionAttributes": {},
    "userAgent": "ask-nodejs/1.0.25 Node/v6.10.3"
    }
    print(json.dumps(jj))
    return app.response_class(json.dumps(jj), content_type='application/json')

def horoscopeTimeAPLNoSign(document, dataSources):
    dataSources = dataSources
    text = "Please try, Alexa, ask horoscope time to give horoscope for leo"
    jj = {
    "version": "1.0",
    "response": {
        "outputSpeech": {
            "type": "SSML",
            "ssml": "<speak>"+text+"</speak>"
        },
        'card': {
            'type': 'Simple',
            'title': "Horoscope Time",
            'content': text
        },
        "directives": [
            {
                "type": "Alexa.Presentation.APL.RenderDocument",
                "document": document,
                "datasources": dataSources,
                "token": "token"
            }
        ],
        "shouldEndSession": True
    },
    "sessionAttributes": {},
    "userAgent": "ask-nodejs/1.0.25 Node/v6.10.3"
    }
    print(json.dumps(jj))
    return app.response_class(json.dumps(jj), content_type='application/json')

if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
        app.config['ASK_APPLICATION_ID'] = ASK_APPLICATION_ID
        app.config['ASK_VERIFY_REQUESTS'] = True
        app.config['ASK_VERIFY_TIMESTAMP_DEBUG'] = True
    app.run(debug=True)
