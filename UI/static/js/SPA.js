const SPA = (($) => {
    "use strict"

    let init;
    let _$spa, _$container, _token 

    init = (spa) => {
        _$spa = $(spa); 
        ResponseModule.getPlayerToken()
        .then((token) => {
            _token = token
        })
        .then(() => {
            ResponseModule.joinGame(_token)
            .then((responseJsonString) => {
                let gameJson = JSON.parse(responseJsonString);
                let gameColumns = gameJson['gameColumns'];
                let gameGrid = JSON.parse(gameJson['gameGrid']);
                let gameToken = gameJson['gameToken'];
                $('#Title').append(gameJson['playerColor'] == -1 ? ' (b)' : ' (w)');
                _$container = $('<div id="reversi-board-container">');
                _$spa.append(_$container);
                GameModule.init(_$container, gameColumns, gameGrid);
            })
            .then(() => {
                // move event handlers
                const fields = $(_$container).find('.reversi-field');
                $(fields).on('click', (ev) => {
                    let data = $(ev.target).data();
                    makeMove(data['col'], data['row']);
                });
            })
            .then(() => {
                Listening();
            });
        });

        
        // game info button
        let btn = $('<input type="button" value="log data from test game" >');
        $(btn).on('click', function(){
            getGameInfo(0);
        });

        let surrenderBtn = $('<input type="button" value="Surrender>"');
        $(surrenderBtn).on('click', () => {

        });

        _$spa.append(btn);
    }

    let makeMove = (col, row) => {
        return new Promise((resolve, reject) => {
            ResponseModule.move(0, col, row, _token)
            .catch(() => {
                alert('something went wrong.');
            });
        });
    }

    let getGameInfo = (token) => {
        return new Promise((resolve, reject) => {
            let gameInfoPromise = ResponseModule.getGameInfo(token);
            Promise.all([gameInfoPromise])
            .then((gameInfo) => {
                console.log(gameInfo);
            })
            .catch(() => {
                alert('something went wrong');
            });
        });
    }

    //Listen for move
    let Listening = () => {
        ResponseModule.listen(_token, GameModule.updateGrid);
    }

    return {
        init : init
    }
})($);

