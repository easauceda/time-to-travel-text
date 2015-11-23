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

**Before you do anything**, you will need an api key from google. You can get one [here](https://developers.google.com/maps/documentation/directions/get-api-key).  

 1. Clone this repository
 2. Start the script `python time_to_home.py`. Enter your information as the program prompts you.
 3. Once done, the script will exit.
 4. Change the schedule in the script, this is inside the main function. There is a comment at its location.
 5. Once done, rerun the script. It should now persist, and will fire a message at your desired time.
