from flask import Flask, request, jsonify
import requests
import json
import urllib
import numpy as np
import datetime


app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Check the wheater forecast! For example /api/wheather_forecast/?location=Leiden&period=2'

if __name__ == '__main__':
  app.run()
