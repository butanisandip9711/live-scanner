from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():

    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=RELIANCE.NS,TCS.NS,INFY.NS"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    data = r.json()

    result = []

    for s in data["quoteResponse"]["result"]:
        result.append({
            "symbol": s["symbol"],
            "price": s["regularMarketPrice"],
            "change": s["regularMarketChangePercent"]
        })

    return jsonify(result)


app.run(host="0.0.0.0", port=10000)
