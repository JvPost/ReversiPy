const SPA = (($) => {
    "use strict"

    let init;
    let _$spa, _$container, _token 

    init = (spa) => {
        _$spa = $(spa); 
        let tokenPromise = SPA.ResponseModule.getPlayerToken;
        let gamePromise = SPA.ResponseModule.joinGame;

        tokenPromise().then((tokenData) => {
            _token = tokenData['playerToken'];
            gamePromise(tokenData['playerToken']).then((gameData) => {
                let gameColumns = gameData['gameColumns'];
                let gameGrid = gameData['gameGrid'];
                let gameToken = gameData['gameToken'];
                $('#Title').append(gameData['playerColor'] == -1 ? ' (b)' : ' (w)');
                _$container = $('<div id="reversi-board-container">');
                _$spa.append(_$container);
                SPA.GameModule.init(_$container, gameColumns, gameGrid);
            }).then(() => {
                // move event handlers
                const fields = $(_$container).find('.reversi-field');
                $(fields).on('click', (ev) => {
                    let data = $(ev.target).data();
                    makeMove(data['col'], data['row']);
                });
            })
            .then(() => {
                listening();
            })
            .then(() => {
                $("#splash-container").css("display", "none");
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
        let p = new Promise((resolve, reject) => {
            SPA.ResponseModule.move(0, col, row, _token)
            .catch(() => {
                alert('something went wrong.');
            });
        });
        return p
    }

    let getGameInfo = (token) => {
        return new Promise((resolve, reject) => {
            let gameInfoPromise = SPA.ResponseModule.getGameInfo(token);
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
    let listening = () => {
        SPA.ResponseModule.listen(_token, SPA.GameModule.updateGrid);
    }

    return {
        init : init,
        listening: listening
    }
})($);

