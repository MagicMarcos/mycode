#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from random import randint
from questions import questions # import questions list
app = Flask(__name__)


@app.route("/")
def trivia():
    '''Renders html page containing a random trivia question'''
    # generate random index
    question_index = randint(0, len(questions)-1)
    #list contaning question and it's index in questions list
    question_list = [list(questions[question_index].keys())[0], question_index]
    #render html and pass in question list
    return render_template('index.html', question = question_list)

@app.route("/result/<name>/<index>/<answer>")
def result(name, index,answer):
    # define result list, this will contain information to be rendered
    result = [name.title()]
    #define list that will contain information of users correct or wrong answers
    question_result=[]
    #collect question from questions list 
    # - note: index is originally a string and must be converted
    idx = int(index)
    question_key = questions[idx].keys()
    # convert dict object into a list and grab the question string
    question = list(question_key)[0]
    
    # conditional logic determines contents of question_result list
    if(questions[idx].get(question) == answer):
        # assign 'correct' string and users answer to question_result 
        question_result = ["correct", answer.title()]
    else:
        #assign 'wrong' string and users answer to question_result
        question_result = ["wrong", answer.title()]

    # use extend method to add question_result list to result list
    result.extend(question_result)

    #render html with the result of users answer
    return render_template("answer.html", result = result)

@app.route("/answer", methods=['POST'])
def answer():
    """Handles post request. 
        > takes in information from submitted form
        > redirects to result function where html page is rendered 
    """
    # store user name and normalize capitalization
    name = request.form.get('name').lower()
    #store users answer and normalize capitalization
    answer =request.form.get('answer').lower()
    #store questions index
    question_idx = request.form.get('q_idx')
    # define path to where user is redirected to
    path = f"/result/{name}/{question_idx}/{answer}"
    # redirect user
    return redirect(path)
    

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 2224)