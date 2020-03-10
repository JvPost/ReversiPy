from flask import Flask, render_template
import redis
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GeheimL0l!'

app.config.from_object(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reversi")
def reversi():
    return render_template(
        "reversi.html"
    )

if __name__ == "__main__":
    app.run(
        port = 5000,
        debug= True
    )