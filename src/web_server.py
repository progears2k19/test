from flask import Flask

app = Flask(__name__)

@app.route("/test")
def tree():
    return {"test": "master"}
