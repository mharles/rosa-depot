import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "dev")


@app.get("/")
def index():
    return jsonify(service="rosa-depot", msg="Depoul e deschis.", version=VERSION)


@app.get("/healthz")
def healthz():
    # Liveness/readiness ieftin: NU verifica dependențe externe aici.
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
