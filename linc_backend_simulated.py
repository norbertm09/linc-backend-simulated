
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/v1/auth/register", methods=["POST"])
def register():
    data = request.json
    return jsonify({
        "status": "success",
        "message": "Utilisateur enregistré",
        "user": {
            "email": data.get("email"),
            "type": data.get("type", "user")
        },
        "token": "simulated_jwt_token_123456"
    })

@app.route("/v1/auth/login", methods=["POST"])
def login():
    return jsonify({
        "status": "success",
        "message": "Connexion réussie",
        "token": "simulated_jwt_token_123456"
    })

@app.route("/v1/wallets", methods=["GET"])
def wallets():
    return jsonify({
        "wallets": [
            {"currency": "CDF", "balance": 100000},
            {"currency": "USD", "balance": 250},
            {"currency": "EUR", "balance": 180}
        ]
    })

@app.route("/v1/transfer/simulate", methods=["POST"])
def transfer_simulate():
    data = request.json
    return jsonify({
        "status": "success",
        "message": "Transfert simulé",
        "to": data.get("to"),
        "amount": data.get("amount"),
        "currency": data.get("currency"),
        "reference": "SIMULATED123456"
    })

@app.route("/v1/card/create", methods=["POST"])
def create_card():
    return jsonify({
        "status": "success",
        "message": "Carte virtuelle créée",
        "card": {
            "type": "Visa",
            "masked_pan": "**** **** **** 1234",
            "expiry": "12/2026"
        }
    })

@app.route("/v1/aml/simulate-check", methods=["POST"])
def aml_check():
    data = request.json
    return jsonify({
        "name_checked": data.get("name"),
        "result": "clear",
        "source": "OpenSanctions (sandbox)"
    })

@app.route("/v1/feedback", methods=["POST"])
def feedback():
    data = request.json
    return jsonify({
        "status": "received",
        "message": data.get("message")
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
