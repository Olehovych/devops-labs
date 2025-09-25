from flask import Flask, jsonify

app = Flask(__name__)

# Головна сторінка
@app.route("/")
def hello():
    return "Hello from Flask in Docker!"

# Статус сервісу
@app.route("/status")
def status():
    return "OK"

# Привітання по імені
@app.route("/hello/<name>")
def greet(name):
    return f"Hello, {name}!"

# Повернення JSON
@app.route("/json")
def json_data():
    return jsonify({"service": "flask-app", "status": "running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
