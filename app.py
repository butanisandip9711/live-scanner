from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        symbols = ["RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS"]

        stocks = []

        for sym in symbols:
            url = f"https://financialmodelingprep.com/api/v3/quote-short/{sym}?apikey=demo"

            r = requests.get(url, timeout=10)
            data = r.json()

            if len(data) > 0:
                stocks.append({
                    "symbol": sym,
                    "price": data[0]["price"]
                })

        return jsonify(stocks)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
