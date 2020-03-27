from flask import Flask, render_template, send_file, send_from_directory
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'GeheimL0l!'
app.config['ENV'] = 'development'
app.config.from_object(__name__)

root = os.path.dirname(os.path.realpath(__file__)) + "\\dist"

@app.route('/<path:path>', methods=["GET"])
def static_proxy(path):
    return send_from_directory(root, path)

@app.route("/", methods=["GET"])
def index():
    return send_from_directory(root, "index.html")

## should be removed
@app.route("/reversi")
def reversi():
    return send_from_directory(root, "reversi.html")
    # return send_file(path+"/reversi.html") # Kunnen we de gulp file structure gebruiken, misschien beter

if __name__ == "__main__":
    app.run(
        port= 5000,
        debug= True
    )