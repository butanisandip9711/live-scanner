from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        symbols = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]

        stocks = []

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        for sym in symbols:
            url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={sym}"

            r = requests.get(url, headers=headers, timeout=10)

            if r.status_code != 200:
                continue

            data = r.json()

            result = data.get("quoteResponse", {}).get("result", [])

            if not result:
                continue

            price = result[0].get("regularMarketPrice")

            stocks.append({
                "symbol": sym,
                "price": price
            })

        return jsonify(stocks)

    except Exception as e:
        return jsonify({"error": str(e)})
