# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:58:12 2020

@author: sas46
"""
# Import packages and create the app
from flask import Flask, render_template, request
app = Flask(__name__)

# Homepage
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Rendering a template by passing in information
@app.route('/test')
def test():
    return render_template('index.html', name="Saniyah", hackathon="Femmehacks")

# Handling a POST request by getting data and sending back a page.
@app.route('/form', methods = ["POST", "GET"])
def post():
    username = request.form.get("username")
    return render_template('success.html', username=username)

# A normal page (no variables to render)
@app.route('/signup')
def root():
    return render_template('signup.html')

# Run the app when you run this file
if __name__ == "__main__":
    app.run()