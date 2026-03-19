from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/qu/quote/RELIANCE.NS"

    headers = {
        "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": os.environ.get("RAPIDAPI_HOST")
    }

    r = requests.get(url, headers=headers)

    data = r.json()

    return jsonify(data)

app.run(host="0.0.0.0", port=10000)
