from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=RELIANCE.NS,TCS.NS,INFY.NS"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(url, headers=headers, timeout=10)

        data = r.json()

        result = data.get("quoteResponse", {}).get("result", [])

        stocks = []

        for s in result:
            stocks.append({
                "symbol": s.get("symbol"),
                "price": s.get("regularMarketPrice"),
                "change": s.get("regularMarketChangePercent")
            })

        return jsonify(stocks)

    except Exception as e:
        return jsonify({"error": str(e)})

