from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Ramjith Docker Flask Demo</h2><p>Running in Docker container.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
