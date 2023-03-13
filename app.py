from flask import Flask

app = Flask(__name__)


@app.route("/encipher")
def encipher():
    return "<p>encipher!</p>"


@app.route("/decipher")
def decipher():
    return "<p>decipher</p>"
