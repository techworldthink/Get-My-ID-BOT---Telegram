import json
import requests


# IMPORTANT -> CHANGE THIS LINE
TELE_TOKEN='paste your bot token here'

URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)

def send_message(text, chat_id):
    final_text = "Telegram Chat ID is :  " + text
    url = URL + "sendMessage?text={}&chat_id={}".format(final_text, chat_id) 
    requests.get(url)

def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    msge = message['message']['text']
    if(msge=="/start"):
        send_message(str(chat_id),chat_id)
    return {
        'statusCode': 200
    }
