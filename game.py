from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
    if request.method == 'PUT':
        #   Stuurt het veld naar de server waar een fiche wordt geplaatst.
        #   Het token van het spel en speler moeten meegegeven worden.
        #   Ook passen moet mogelijk zijn.
        print(request.data)
        response.status_code = 200
    else:
        response.status_code = 400

    print(response)
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