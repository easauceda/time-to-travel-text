import requests
import json
import time
import schedule
import smtplib

with open('config-git.json', 'r') as conf:
    config = json.load(conf)


API_KEY = config['api_key']
USERNAME = config['username']
PW = config['password']
TO = config['recipient']
URL = """https://maps.googleapis.com/maps/api/directions/json?origin=228+Main+
Street+Venice,+CA&destination=16320+E+Clovermead+St+Covina,+CA+91722
&departure_time=now&key=""" + API_KEY


def getETA():
    r = requests.get(URL)
    parsed_r = json.loads(r.text)
    eta = parsed_r["routes"][0]["legs"][0]["duration_in_traffic"]["text"]
    message = "It will take " + eta + " to get home."
    send(message)


def send(message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(USERNAME, PW)
    try:
        server.sendmail(USERNAME,
                        TO, message)
    except:
        print "something went wrong"


schedule.every().day.at("21:46").do(getETA)

while True:
    schedule.run_pending()
    time.sleep(1)
