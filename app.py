from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from my Flask App!</h1><p>Managed by GitHub.</p>"

if __name__ == "__main__":
    app.run(debug=True)