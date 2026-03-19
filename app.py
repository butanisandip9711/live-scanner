from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=RELIANCE.NS,TCS.NS,INFY.NS,HDFCBANK.NS,ICICIBANK.NS"

    data = requests.get(url).json()

    stocks = []

    for s in data["quoteResponse"]["result"]:
        stocks.append({
            "symbol": s["symbol"],
            "price": s["regularMarketPrice"],
            "change": s["regularMarketChangePercent"]
        })

    return jsonify(stocks)

app.run(host="0.0.0.0", port=10000)
