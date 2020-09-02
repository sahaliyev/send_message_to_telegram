"""
1. Open telegram and search for BotFather
2. type '/newbot' to start your bot (give a name to it)
3. choose username for your bot (please consider it should end with bot, example my_bot, mybot)
4. You will get token like this, '4567703444:AAGJ9csdfggkE8rTYH_kM5pNDYaLM0-GW80'
5. search for userinfobot and get your id from there which will be chat_id below
"""

import requests


def send_hello(message):
    token = '4567703444:AAGJ9csdfggkE8rTYH_kM5pNDYaLM0-GW80'  # step 4 value
    chat_id = [1]  # you may send more than one person by adding more id (step 5 value)
    for c_id in chat_id:
        url_req = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={c_id}&text={message}'
        result = requests.get(url_req)
        print(result.json())


txt = "Hello There"
send_hello(txt)
