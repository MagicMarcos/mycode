#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/start")
def trivia():
    return render_template('index.html')

@app.route("/correct")
def correct():
    return render_template("correct.html")

@app.route("/answer", methods=['POST'])
def answer():
    answer =request.form.get('answer')
    path = ''

    if answer == "Harry Potter":
        path = "/correct"
    else:
        path = "/start"
    return redirect(path)

    # SOLUTION using url_for 
    # if answer == "Harry Potter":
    #     path = "correct" # We enter the function name and not the route
    # else:
    #     path = "trivia" # function name -- not ROUTE
    # return redirect(url_for(path))
    

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 2224)