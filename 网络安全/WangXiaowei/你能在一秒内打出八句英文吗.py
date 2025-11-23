from http.client import responses

import requests
from bs4 import BeautifulSoup
from paramiko.agent import value
from requests import session

session = requests.Session()

url = "https://eci-2ze9zjsy2qfnt1r1vy80.cloudeci1.ichunqiu.com:80/start"
responses = session.get(url)

if responses.status_code == 200:
    soup = BeautifulSoup(responses.text,'html.parser')
    text_element = soup.find('p',id='text')
    if text_element:
        value = text_element.get_text()
        print(f"{value}")
        submit_url = "https://eci-2ze9zjsy2qfnt1r1vy80.cloudeci1.ichunqiu.com:80/submit"
        payload = {'user_input':value}
        post_response = session.post(submit_url,data=payload)
        print(post_response.text)
else:
    print(f"{responses.status_code}")

