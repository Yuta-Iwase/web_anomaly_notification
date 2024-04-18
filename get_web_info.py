import os
import requests
import json
from bs4 import BeautifulSoup

url = 'https://weather.com/weather/today/l/aac619af0e4a1f0ffbab44e0cd35501d61e2c5d4337767432f5cbac90957d7a1'
selector = 'div[data-testid="wxPhrase"]'
usual_text_value = 'Fair'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tracking_text = soup.select_one(selector).text
tracking_text = tracking_text.replace('\n','')

if not(tracking_text==usual_text_value):
    msg = f"Anomaly detected.\nContent: {tracking_text}"
    webhook_url = os.environ.get('WEBHOOK_URL')
    data = {"text": msg}
    headers = {
        'Content-type': 'application/json',
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)