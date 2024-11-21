from datetime import datetime

from flask import Flask, request

app = Flask(__name__)


@app.route("/health")
def health():
    return {"status": "OK"}, 200


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return data


@app.route("/time")
def time():
    return {"server_time": datetime.utcnow()}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
