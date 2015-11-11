#Time To Travel!
##Automate the traffic check

###What does it do?
This script will query the Google Maps API and send a text to your phone with the estimated travel time.

###How does it do it?

 1. Request to Google Maps API
 2. Parse response for duration_in_traffic
 3. Email your phone the results, which comes through as a text

###Why?

I got tired of checking the traffic every day before I left work. It was just an extra step I didn't need. So why not automate it? 

###How do I run it?

Before you do anything, you will need an api key from google. You can get one [here](https://developers.google.com/maps/documentation/directions/get-api-key).  

 1. Clone this repository
 2. Enter your information
   * `API_KEY`: Your api key obtained from google.
   * `USERNAME`: your email address, will be used to log in and send the text
   * `PW`: Your email password
   * `TO`: Phone Number + gateway adress. SMS or MMS gateway can be found [here](https://en.wikipedia.org/wiki/SMS_gateway#Use_with_email_clients)
   * `FROM`: This can be set to anything, doesn't have an effect on the message
 3. Edit the URL to the locations of your choosing. Information can be found [here](https://developers.google.com/maps/documentation/directions/intro)
 4. Save, and run: `python time_to_home.py`
