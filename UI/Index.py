from flask import Flask, render_template, send_file


app = Flask(__name__)

app.config['SECRET_KEY'] = 'GeheimL0l!'
app.config['ENV'] = 'development'
app.config.from_object(__name__)

path = ""

if (app.config['ENV'] == 'production'):
    path = "./dist"
else:
    path = "./src"
    


@app.route("/")
def index():
    # return render_template("index.html")
    return send_file(path+"/index.html") # Kunnen we de gulp file structure gebruiken, misschien beter

@app.route("/reversi")
def reversi():
    # return render_template("reversi.html")
    return send_file(path+"/reversi.html") # Kunnen we de gulp file structure gebruiken, misschien beter

if __name__ == "__main__":
    app.run(
        port= 5000,
        debug= True
    )