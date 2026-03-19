from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=RELIANCE.NS,TCS.NS,INFY.NS,HDFCBANK.NS,ICICIBANK.NS"

        r = requests.get(url, timeout=10)

        if r.status_code != 200:
            return jsonify({"error": "API not responding"}), 500

        data = r.json()

        stocks = []

        for s in data.get("quoteResponse", {}).get("result", []):
            stocks.append({
                "symbol": s.get("symbol"),
                "price": s.get("regularMarketPrice"),
                "change": s.get("regularMarketChangePercent")
            })

        return jsonify(stocks)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
