from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        symbols = ["RELIANCE.NS","TCS.NS","INFY.NS"]

        stocks = []

        for sym in symbols:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"

            r = requests.get(url, timeout=10)
            data = r.json()

            result = data["chart"]["result"][0]

            price = result["meta"]["regularMarketPrice"]

            stocks.append({
                "symbol": sym,
                "price": price
            })

        return jsonify(stocks)

    except Exception as e:
        return jsonify({"error": str(e)})
