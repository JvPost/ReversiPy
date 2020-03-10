let ResponseModule = (($) => {
    "use strict"

    let move, getGameInfo, getPlayerToken, joinGame, getGameInfoFromPlayerToken;
    let _path = "http://localhost:5001";
    

    // movetype, row, col
    move = (moveType, col, row) => {
        return new Promise((resolve, reject) => {
            $.ajax({
                url: _path + '/api/Spel/Zet',
                method: 'PUT',
                data: JSON.stringify({ 
                    moveType: moveType,
                    col: col,
                    row: row
                }),
                success: (data) => {
                    resolve(data);
                },
                failed: (data) => {
                    reject('failed');
                }
            });
        });
    }

    getGameInfo = (token = 0) => {
        return new Promise((resolve, reject) => {
            $.ajax(_path + '/api/Spel/' + token, {
                success: (data) => {
                    resolve(data);
                },
                failed: (data) => {
                    reject('failed');
                }
            });
        });
    }

    getPlayerToken = () => {
        return new Promise((resolve, reject) => {
            $.ajax(_path + '/api/Spel/GetPlayerToken',
            {
                method: 'GET',
                success: (data) => {
                    resolve(data);
                },
                failed: (data) => {
                    reject('failed');
                }
            });
        });
    }

    joinGame = (token) => {
        return new Promise((resolve, reject) => {
            $.ajax({
                url: _path + '/api/Spel/JoinGame',
                method: 'PUT',
                data: JSON.stringify({
                    token: token
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

    getGameInfoFromPlayerToken = (token) => {
        return new Promise((resolve, reject) => {
            $.ajax({
                // TODO
            });
        });
    }

    return {
        move : move,
        getGameInfo: getGameInfo,
        getPlayerToken : getPlayerToken,
        joinGame: joinGame,
        getGameInfoFromPlayerToken: getGameInfoFromPlayerToken
    };
})($);