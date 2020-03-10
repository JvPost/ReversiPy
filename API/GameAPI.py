from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json 
import redis
import uuid

from GameClass import Game


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'GeheimL0l!'

rServer = redis.Redis(host="localhost", port = 6379, db=0)

games = {}


@app.route('/api/Spel/<token>', methods = ['GET', 'POST'])
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
                game = games['0']
                game.update(0, reqDict['row'], reqDict['col'])
            response.status_code = 200
        except Exception:
            response.status_code = 401
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

@app.route('/api/Spel/GetPlayerToken', methods = ['GET'])
def getPlayerToken():
    remoteIP = request.remote_addr
    remoteBrowser = request.user_agent.browser
    key = remoteIP + '-' + remoteBrowser
    token = str(uuid.uuid4())
    rServer.set(key, token)
    return token 

@app.route('/api/Spel/JoinGame', methods = ['PUT'])
def joinGame():
    response = Response()
    response.status_code = 400
    if request.method == 'PUT':
        reqDict = RequestDataDict(request.get_data())
        playerToken = reqDict['token']
        if (any(game.white == playerToken or game.black == playerToken for game in games.values())): # already in game
            response.status_code = 200
            raise('should not be possible right now')
        elif (len(games) % 2 != 0): # join existing game TODO: spawn push stuff
            response.status_code = 200
            raise('should not be possible yet')
        else: # new game
            newGameToken = str(uuid.uuid4())
            game = Game(newGameToken, playerToken, None)
            games[newGameToken] = game
            response.set_data(str(game.grid).replace("'", '"'))
            # TODO: spawn push stuff
            response.status_code = 201
            
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