import requests
import json
import time
import schedule
import smtplib
import os.path


def init_config():
    dict_conf = {
        "base_url": "https://maps.googleapis.com/maps/api/directions/json?origin=",
        "url_suffix": "&departure_time=now&key="
    }
    dict_conf['username']= raw_input("Enter your email username: ")
    dict_conf['password'] = raw_input("Enter your email password: ")
    dict_conf['recipient'] = raw_input("Enter the phone number + gateway you would like to use: ")
    print("NOTE: For the following, any spaces MUST be entered as '+'. ")
    print("For example, 123 Main St, USA would be 123+Main+St,+USA")
    dict_conf['origin'] = raw_input("Enter the location at which you begin (work, school, etc): ")
    dict_conf['destination'] = raw_input("Enter the destination (home, school, etc): ")
    dict_conf['api_key'] = raw_input("Finally, enter your google maps api key: ")

    with open('config.json', 'w') as conf:
        json.dump(dict_conf, conf)
    conf.closed

    print("Great! We're all set, run it again/")


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

def main():
    # Ensure config has been created & stored, otherwise run init script
    if (os.path.isfile('config.json')):
        global USERNAME
        global PW
        global TO
        global URL

        with open('config.json', 'r') as conf:
            config = json.load(conf)

        USERNAME = config['username']
        PW = config['password']
        TO = config['recipient']
        URL = "{base_url}{origin}&destination={destination}{url_suffix}{api_key}".format(**config)
        print(URL)

    # This is how the job is run on a schedule
        schedule.every().day.at("23:17").do(getETA)

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        init_config()


if __name__ == "__main__":
    main()
