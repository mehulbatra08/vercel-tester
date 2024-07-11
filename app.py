from flask import Flask
from flask import Flask, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/")
def start():
    return "The MBSA Server is Running"

@app.route("/mbsa")
def mbsa():
    return render_template('index.html')
