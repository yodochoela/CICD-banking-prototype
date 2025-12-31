from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "CI/CD Banking Prototype Backend Running"

@app.route("/api/health")
def health():
    return jsonify({"status": "Backend is running"})

@app.route("/api/accounts")
def accounts():
    return jsonify({
        "status": "success",
        "data": [
            {"account_no": 1, "name": "Yordanos Mesfin", "balance": 10000},
            {"account_no": 2, "name": "Natnael Abebe", "balance": 5000}
        ]
    })

if __name__ == "__main__":
    app.run(debug=False)

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/health")
def health():
    return jsonify(status="CI/CD Banking Prototype Backend Running"), 200

if __name__ == "__main__":
    app.run(debug=False)
