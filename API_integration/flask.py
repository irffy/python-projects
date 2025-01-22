from flask import Flask 

app = Flask(__name__)

@app.route("/")
def func2():
    return "Hello Irfan"

app.run("0.0.0.0",5000)   