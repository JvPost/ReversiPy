let ResponseModule = (($) => {
    "use strict"

    let move, getGameInfo, getPlayerToken, joinGame, listen;
    let _path = "http://localhost:5001";
    

    // movetype, row, col
    move = (moveType, col, row, playerToken) => {
        return new Promise((resolve, reject) => {
            return $.ajax({
                url: _path + '/api/Spel/Zet',
                method: 'PUT',
                data: JSON.stringify({ 
                    moveType: moveType,
                    col: col,
                    row: row,
                    playerToken: playerToken
                    // TODO: Add game token
                }),
                success: (data) => {
                    resolve(data);
                },
                failed: (data) => {
                    console.log('failed')
                    reject('failed');
                }
            });
        });
    }

    getGameInfo = (token = 0) => {
        return new Promise((resolve, reject) => {
            return $.ajax(_path + '/api/Spel/' + token, {
                success: (data) => {
                    resolve(data);
                },
                failed: (data) => {
                    reject('failed');
                }
            });
        });
    }

    /**
     * Returns promise token for a player token. When the promise succeeds a token is returned, else 'failed' is returned.
     */
    getPlayerToken = () => {
        return new Promise((resolve, reject) => {
            return $.ajax(_path + '/api/Spel/GetPlayerToken',
                {
                    method: 'GET',
                    success: (data) => {
                        resolve(data);
                    },
                    failed: (data) => {
                        reject('failed'); // TODO: add search for game?
                    }
                });
        });
    }

    joinGame = (playerToken) => {
        return new Promise((resolve, reject) => {
            return $.ajax({
                url: _path + '/api/Spel/JoinGame',
                method: 'PUT',
                data: JSON.stringify({
                    playerToken: playerToken
                }),
                success: (data) => {
                    resolve(data);
                },
                failed: () => {
                    reject('failed');
                }
            });
        });
    }

    listen = (playerToken, callback) => {
        var source = new EventSource(_path + '/api/Spel/Event/' + playerToken);
        source.onmessage = (event) => {
            if (event.data != "1"){
                let eventStr = event.data.split("'")[1];
                let eventJson = JSON.parse(eventStr);
                callback(eventJson)
            }
        }
    }
    
    return {
        move : move,
        getGameInfo: getGameInfo,
        getPlayerToken : getPlayerToken,
        joinGame: joinGame,
        listen: listen
    };
})($);