from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():

    stocks = ["RELIANCE", "TCS", "INFY"]

    result = []

    for s in stocks:

        url = f"https://priceapi.moneycontrol.com/pricefeed/nse/equitycash/{s}"

        r = requests.get(url).json()

        result.append({
            "symbol": s,
            "price": r["data"]["pricecurrent"],
            "change": r["data"]["pricechange"]
        })

    return jsonify(result)

app.run(host="0.0.0.0", port=10000)
app.run(host="0.0.0.0", port=10000)
