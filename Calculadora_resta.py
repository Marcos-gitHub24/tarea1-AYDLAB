from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/resta', methods=["POST"])
def add_guide():
    numero1 = request.json["num1"]
    numero2 = request.json["num2"]
    return str(numero1 - numero2)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
    app.run(debug=True)