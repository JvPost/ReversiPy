let ResponseModule = (($) => {
    "use strict"

    let init, move, getGameInfo, getPlayerToken;
    let _path = "http://localhost:5001";
    let _isInit = false;
    
    let init = () => {
        if (!_isInit){
            Promise((reject, resolve) => {
                $.ajax({
                    url: _path + '/api/Spel/GetToken',
                    method: 'GET',
                    success: (data) => {
                        _isInit = true;
                        resolve(data);
                    },
                    failed: () => {
                        reject('No token allowed');
                    }
                })
            }).then((result) => {
                
            }).catch((err) => {
                
            });
        }

        return _isInit;
    }

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
            $.ajax(_path + '')
        });
    }

    return {
        init: init,
        move : move,
        getGameInfo: getGameInfo,
        getToken: getPlayerToken
    };
})($);