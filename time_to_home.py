import requests
import json
import smtplib

API_KEY = ""
USERNAME = ""
PW = ""
TO = ""
FROM = ""
URL = """https://maps.googleapis.com/maps/api/directions/json?origin=Venice,
+CA&destination=Glendale,+CA
&departure_time=now&key=""" + API_KEY

r = requests.get(URL)
parsed_r = json.loads(r.text)

travel_time = parsed_r["routes"][0]["legs"][0]["duration_in_traffic"]["text"]
message = "Going home will take " + travel_time
server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()
server.login(USERNAME, PW)
server.sendmail(FROM, TO, message)
