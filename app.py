from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=RELIANCE.NS"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code != 200:
            return jsonify({"error": "API Status " + str(r.status_code)})

        data = r.json()

        result = data.get("quoteResponse", {}).get("result", [])

        if not result:
            return jsonify({"error": "No Data"})

        stock = result[0]

        return jsonify({
            "symbol": stock.get("symbol"),
            "price": stock.get("regularMarketPrice"),
            "change": stock.get("regularMarketChangePercent")
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
