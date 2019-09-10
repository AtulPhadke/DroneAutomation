from flask import Flask
from flask import render_template, request
import time
import os
app = Flask(__name__)
#! /usr/bin/python

from gps import *
import time
import os

@app.route('/')
def function():
    return render_template("index.html")

@app.route('/power')
def power():
    text = request.args.get('Power')
    return render_template("power.html", text=text)
