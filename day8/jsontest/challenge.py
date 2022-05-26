#!/usr/bin/env python3
import requests 
import json

def main(): 
    IP_URL = "http://ip.jsontest.com/"
    TIME_URL =  "http://time.jsontest.com"

    ip_res = requests.get(IP_URL)
    time_res = requests.get(TIME_URL)

    ip = ip_res.json()
    time = time_res.json()['time']

    with open('myservers.txt', 'r') as servers:
        print(servers.read())
    
if __name__ == "__main__":
    main()