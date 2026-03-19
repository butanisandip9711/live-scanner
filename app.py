from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"

        r = requests.get(url, timeout=10)

        if r.status_code != 200:
            return jsonify({"error": "API status " + str(r.status_code)})

        data = r.json()

        price = data.get("bpi", {}).get("USD", {}).get("rate", "No Data")

        return jsonify({
            "symbol": "BTCUSD",
            "price": price
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
