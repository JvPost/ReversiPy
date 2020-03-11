from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from first import first

import json 
import redis
import uuid


from GameClass import Game


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'GeheimL0l!'

redisPlayerServer = redis.Redis(host="localhost", port = 6379, db=0)
redisStreamServer = redis.StrictRedis(db=1)

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
        game = None
        legalMove = False
        try:
            game = GetGameFromPlayerToken(reqDict['playerToken'])
            if (reqDict['moveType'] == 0): # placing stone
                legalMove = game.update(reqDict['playerToken'], reqDict['row'], reqDict['col'])
            response.status_code = 200
        except Exception as exception:
            print (exception)
            response.status_code = 401
        if (game is not None and legalMove):
            playerColor = -1 if reqDict['playerToken'] == game.black else 1
            json = str(
                {   'moveType': 0,
                    'col': reqDict['col'],
                    'row': reqDict['row'],
                    'playerColor': playerColor }).replace("'", '"')
            redisStreamServer.publish(game.token, json)
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
    token = redisPlayerServer.get(key)
    if (token is None):
        token = str(uuid.uuid4())
        redisPlayerServer.set(key, token)    
    return token 

@app.route('/api/Spel/JoinGame', methods = ['PUT'])
def joinGame():
    response = Response()
    response.status_code = 400
    if request.method == 'PUT':
        reqDict = RequestDataDict(request.get_data())
        playerToken = reqDict['playerToken']
        game = GetGameFromPlayerToken(playerToken)
        if (game is not None): # already in game
            response.status_code = 200                
        elif (len(games) % 2 != 0): # join existing game
            game = first(games.values(), key = lambda g: g.white == None or g.black == None)
            game.addPlayer(playerToken)
            response.status_code = 200
        else: # new game
            newGameToken = str(uuid.uuid4())
            game = Game(newGameToken, playerToken, None)
            games[newGameToken] = game
            
            response.status_code = 201
        
        responseDict = {
                'gameToken': game.token,
                'gameGrid': game.grid,
                'playerColor': -1 if playerToken == game.black else 1
            }

        response.set_data(str(responseDict).replace("'", '"'))
    return response

@app.route('/api/Spel/Event/<playerToken>', methods = ['GET'])
def event(playerToken):
    game = GetGameFromPlayerToken(playerToken)
    if (game is not None):
        return Response(EventStream(game.token), mimetype='text/event-stream')
    else:
        return 'error'

def EventStream(gameToken):
    pubsub = redisStreamServer.pubsub()
    pubsub.subscribe(gameToken) 
    for message in pubsub.listen():
        print (message)
        yield 'data:%s\n\n' % message['data']

def RequestDataDict(requestData):
    reqDataBytes = request.get_data()
    reqDataString = reqDataBytes.decode('utf8').replace("'", '"')
    return json.loads(reqDataString)

def GetGameFromPlayerToken(playerToken):
    for g in games.values():
        if g.black == playerToken or g.white == playerToken:
            return g
    return None

if __name__ == "__main__":
    app.run(
        port = 5001,
        debug=True
    )