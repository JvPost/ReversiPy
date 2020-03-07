from flask import Flask, request, jsonify, Response, session
from flask_cors import CORS
import json 
from GameClass import Game

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

SESSION_TYPE = ''

games = {
    '0': Game(0, 'white', 'black') # TODO: fix
}

@app.route('/api/Spel/GetToken', methods = ['GET'])
def getToken():
    
    return 'token'

@app.route('/api/Spel/<token>', methods = ['GET'])
def getGameInfo(token):
    response = Response()
    if request.method == 'GET':
        #	Omschrijving
        #	Tokens van het spel en van de spelers
        #	bord en elk vakje de bezetting (geen fiche, zwart fische, wit fische)
        #	Wie aan de beurt is
        #	Status van het spel (bijv. De winnaar, opgeven door)
        response.status_code = 200
        return games[token].grid
    else:
        response.status_code = 400

@app.route('/api/Spel/Beurt/<token>', methods = ['GET'])
def beurt(token):
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
    response.status_code = 400
    if request.method == 'PUT':
        #   Stuurt het veld naar de server waar een fiche wordt geplaatst.
        #   Het token van het spel en speler moeten meegegeven worden.
        #   Ook passen moet mogelijk zijn.
        reqDict = RequestDataDict(request.get_data())
        try:
            if (reqDict['moveType'] == 0): # placing stone
                game = games['0'] # TODO add token
                game.update(0, reqDict['row'], reqDict['col'])
            response.status_code = 200
        except Exception: # TODO make specific
            response.status_code = 401 # TODO illegal move status_code maybe? idk yet
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

def RequestDataDict(requestData):
    reqDataBytes = request.get_data()
    reqDataString = reqDataBytes.decode('utf8').replace("'", '"')
    return  json.loads(reqDataString)

if __name__ == "__main__":
    app.run(
        port = 5001,
        debug=True
    )