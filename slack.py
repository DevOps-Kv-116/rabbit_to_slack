import json
import sys
import random
import requests

from config import *


def dataToMessage(data):
    user = data.issue.user.login
    action = data.action

    return f"{user} {action} something in project issues"
    

def sendToSlack(data):
    url = SLACK_URL
    message = dataToMessage(data)
    title = (f"{user} Made new changes")
    slack_data = {
        "icon_emoji": ":rocket:",
        "channel" : SLACK_CHANNEL,
        "attachments": [
            {
                "color": "#5F2C9C",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
