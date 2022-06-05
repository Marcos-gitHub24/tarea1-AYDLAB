from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/informacion', methods=["GET"])
def add_guide():
    return str("Jose Marcos García Olmino - 201903895")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
    app.run(debug=True)