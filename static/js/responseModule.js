SPA.responseModule = (($) => {
    let move, getGameInfo;
    let _path = "http://localhost:5001";
    
    // movetype, row, col
    move = (moveType, col, row) => {
        return new Promise((resolve, reject) => {
            $.ajax(_path + '/api/Spel/Zet',
            {
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

    return {
        move : move,
        getGameInfo: getGameInfo
    };
})($);