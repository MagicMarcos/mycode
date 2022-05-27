#!/usr/bin/env python3
import requests
import json
from pprint import pprint

def json_req(question, answer):
    """Makes post request to /json route
        > allows users to add a new question to trivia game
    """
    if question != "" or answer!= "": # ensure question and answer aren't empty
        # define route where post req eill be made
        URL = "https://aux1-9591a944-4a65-4519-b3a1-0795ea929524.live.alta3.com/json"

        # users new question
        new_question = {
                "question": question,
                "answer": answer,
                }

        # a url to send the request 
        # and a json string to attach to the request
        resp= requests.post(URL, json=new_question)
    else: 
        # print empty string error 
        print(f"Question: '{question}' or Answer: '{answer}' supplied are empty.\nIf this module was called directly, please note this module is intended to be called indirectly ")

if __name__ == "__main__":
    # define default values for question and answer - used for error hadling
    question = ""
    answer = ""
    json_req(question, answer)