# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:58:12 2020

@author: sas46
"""

from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return render_template('index.html', name="Saniyah", hackathon="Femmehacks")

@app.route('/form', methods = ["POST", "GET"])
def post():
    username = request.form.get("username")
    return render_template('success.html', username=username)

@app.route('/signup')
def root():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run()