#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify
from random import randint
from alta3research_requests02 import json_req
from questions import trivia_questions # import questions list
import json
import yaml

app = Flask(__name__)

# read questions from json -> load givens us python obj
questions = ''
with open("questions.json", "r") as questions_file:
    questions = json.load(questions_file)

@app.route("/")
def trivia():
    '''Renders html page containing a random trivia question'''
    # generate random index
    question_index = randint(0, len(questions)-1)
    #list contaning question and it's index in questions list
    question_list = [questions[question_index].get('question'), question_index]
    #render html and pass in question list
    return render_template('index.html', question = question_list)

@app.route("/result/<name>/<index>/<answer>")
def result(name, index,answer):
    """ Handles logic for displaying result:
            > takes in user name, question index and answer
            > runs conditional logic to determine answer result
            > render HTML with appropriate response
    """

    # define result list, this will contain information to be rendered
    result = [name.title()]
    #define list that will contain information of users correct or wrong answers
    question_result=[]

    # conditional logic determines contents of question_result list
    if(questions[int(index)].get("answer") == answer):
        # assign 'correct' string and users answer to question_result 
        question_result = ["correct", answer.title()]
    else:
        #assign 'wrong' string and users answer to question_result
        question_result = ["wrong", answer.title()]

    # add question_result list to result list
    result.extend(question_result)
    #render html with the result of users answer
    return render_template("answer.html", result = result)

@app.route("/answer", methods=['POST'])
def answer():
    """Handles post request for answers. 
        > takes in information from submitted form
        > redirects to result function where html page is rendered 
    """
    path = "/"
    # store user name and normalize capitalization
    name = request.form.get('name').lower()
    #store users answer and normalize capitalization
    answer =request.form.get('answer').lower()
    #store questions index
    question_idx = request.form.get('q_idx')

    if name != "" and answer != "" and question_idx != "" :
        # define path to where user is redirected to
        path = f"/result/{name}/{question_idx}/{answer}"

    # redirect user
    return redirect(path)

@app.route('/json', methods=["GET","POST"])
def json_data():
    """Handles GET and POST request to /json route:
        > GET: simply presents json obj with all questions
        > POST: adds question to list, updates both json and yaml files
    """
    if request.method == "POST": # ensure a post req is being made
        data=request.json # grab json data
        
        if data:
            # both dumps and loads we're needed to avoid type errors
            data = json.dumps(data) # python obj to json str
            data = json.loads(data) # json str to python obj

            question = data["question"] # collect question from data
            answer = data["answer"] # collect answer from data

            # append to questions list
            questions.append({"question": question, "answer" : answer})

        # open json file and dump updated questions to file
        with open("questions.json", "w") as questions_file:
            json.dump(questions, questions_file)

        # open yaml file and dump updated questions to file
        with open("questions.yaml", "w") as questions_yaml:
            yaml.dump(questions, questions_yaml)

    # jsonify questions and pass in to browser on GET requests
    return jsonify(questions)

@app.route('/addquestion', methods=["POST"])
def add_question():
    """ Handles logic for adding questions to list:
        > gets user information from form, and calls json_req function
        > redirects user to home page
    """
    if request.method == "POST": # prevent accidental GET requests
        question = request.form.get('question') # collect question
        answer = request.form.get('answer') # collect answer

        # call json_req, passing in question and answer
        # json_req, uses requests module to POST to /json route and update json and yaml files
        json_req(question, answer) 

    return redirect('/') # redirect home

@app.route('/cheater')
def see_all_questions():
    """Renders html containing all questions and answers"""
    return render_template("all_questions.html", questions = questions)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 2224)