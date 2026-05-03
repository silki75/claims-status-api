from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/claims/<claim_id>")
def get_claim(claim_id):
    return jsonify({
        "claim_id": claim_id,
        "status": "Approved",
        "source": "claims-status-api"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)