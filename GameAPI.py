from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json 
from GameClass import Game

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

games = {
    '0': Game(0, 'white', 'black') # TODO: fix
}

@app.route('/api/Spel/Token', methods = ['GET'])
def token():
    response = Response()
    if request.method == 'GET':
        #	Omschrijving
        #	Tokens van het spel en van de spelers
        #	bord en elk vakje de bezetting (geen fiche, zwart fische, wit fische)
        #	Wie aan de beurt is
        #	Status van het spel (bijv. De winnaar, opgeven door)
        
        response.status_code = 200
    else:
        response.status_code = 400
    return response

@app.route('/api/Spel/Beurt/<token>', methods = ['GET'])
def beurt():
    response = Response()
    if request.method == 'GET':
        #logic
        response.status_code = 200
    else:
        response.status_code = 400
    return response


@app.route('/api/Spel/Zet', methods = ['PUT'])
def move():
    response = Response()
    response.status_code = 400;
    if request.method == 'PUT':
        #   Stuurt het veld naar de server waar een fiche wordt geplaatst.
        #   Het token van het spel en speler moeten meegegeven worden.
        #   Ook passen moet mogelijk zijn.
        reqDataBytes = request.get_data()
        reqDataString = reqDataBytes.decode('utf8').replace("'", '"')
        reqJson = json.loads(reqDataString)

        if (games['0'] is not None): #check if exists TODO fix
            game = games['0']
            print(game.grid)
            response.status_code = 200

    return response

@app.route('/api/Spel/Opgeven', methods = ['PUT'])
def giveUp():
    response = Response()
    if request.method == 'PUT':
        #logic
        response.status_code = 200
    else:
        response.status_code = 400
    return response

if __name__ == "__main__":
    app.run(
        port = 5001,
        debug=True
    )