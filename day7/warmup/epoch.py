#!/usr/bin/env python3
"""A morning challenge with several bonuses"""

import requests
import time
import reverse_geocoder

# challenge1: Using the requests module, access the API from the link and pull/translate the JSON!
# challenge2: This API changes EVERY SINGLE TIME a GET request is sent to it (it's moving 4.76 miles per second, after all!) Make your script return the collected data into something like this:
# challenge3: This API also returns the timestamp of when the response was generated in Epoch time. Return this value, but make it human readable 
# challenge4: You've got the location... but that's not very human readable, is it? What CITY and COUNTRY is the ISS currently flying across? Take a look at the 3rd party library reverse_geocoder- there is
# API link: http://api.open-notify.org/iss-now.json

def get_ISS_json():
    """Function retrieves ISS data from api and parses JSON as dictionary"""

    url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url)
    return res.json()

def get_location():
    """Retrieves location information from API and returns as a fstring"""
    
    # call get_ISS_json() function to get needed data
    data = get_ISS_json()

    # collect latitude and longitude from data dictionary returned
    longitude = data.get("iss_position").get("longitude")
    latitude = data.get("iss_position").get("latitude")

    # use reverse_geocoder module to get accurate location info -- must pass in lon and lat as tuple
    coordinate_tuple = (latitude, longitude)
    location = reverse_geocoder.search(coordinate_tuple)
    
    # store relevant location info into variables
    name = location[0].get('name')
    state_or_province = location[0].get('admin1')
    country_code = location[0].get('cc')

    # format data and return as string
    return f"\nLon: {longitude} \nLat: {latitude} \nCity/Country: {name}, {state_or_province}, {country_code}"
    
def collected_data():
    """Collects all relevant data about ISS (Current time, longitude, latitude and location) and prints"""

    # get dictionary of data from API
    data = get_ISS_json()

    # collect epoch time from dictionary and format timestamp into human readable time
    epoch_timestamp = data.get("timestamp")
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_timestamp))
    
    # call location function to retrieve location string
    location = get_location()

    # format and print final string to console
    print("\n========================================\n")
    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {timestamp} {location}")

def main():
    """main function calls collected_data() and sets starts the program"""

    # calls collected_data() which prints a string with all relevant information
    collected_data()

if __name__ == "__main__":
    main()