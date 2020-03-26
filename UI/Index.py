from flask import Flask, render_template
import redis
import uuid
import sys


app = Flask(__name__)

app.config['SECRET_KEY'] = 'GeheimL0l!'
app.config['ENV'] = 'development'
app.config.from_object(__name__)

if (app.config['ENV'] == 'production'):
    app.template_folder = app.template_folder + '/dist'
else:
    app.template_folder = app.template_folder + '/src'
    


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reversi")
def reversi():
    return render_template("reversi.html")

if __name__ == "__main__":
    app.run(
        port= 5000,
        debug= True
    )