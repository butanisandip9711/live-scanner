from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():

    symbols = [
        "RELIANCE",
        "TCS",
        "INFY"
    ]

    data_list = []

    for s in symbols:

        url = f"https://priceapi.moneycontrol.com/techCharts/indianMarket/stock/history?symbol={s}&resolution=1D&from=1680000000&to=1890000000"

        r = requests.get(url).json()

        price = r["c"][-1]

        data_list.append({
            "symbol": s,
            "price": price
        })

    return jsonify(data_list)


app.run(host="0.0.0.0", port=10000)
