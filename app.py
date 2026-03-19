from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

        r = requests.get(url, timeout=10)

        if r.status_code != 200:
            return jsonify({"error": "API Status " + str(r.status_code)})

        data = r.json()

        return jsonify({
            "symbol": data.get("symbol"),
            "price": data.get("price")
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
