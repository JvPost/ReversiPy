const SPA = (($) => {
    "use strict"

    let init;
    let _$spa, _$container, _token 

    init = (spa) => {
        _$spa = $(spa); 
        let tokenPromise = SPA.ResponseModule.getPlayerToken;
        let gamePromise = SPA.ResponseModule.joinGame;

        tokenPromise()
            .then((data) => {
                _token = data['playerToken'];
                return _token;
            })
            .then((token) => {
                return gamePromise(token)
            })
            .then((data) => {
                const columns = data['gameColumns'];
                const grid = data['gameGrid'];
                const gameToken = data['gameToken'];
                $('#Title').append(data['playerColor'] == -1 ? ' (b)' : ' (w)');
                _$container = $('<div id="reversi-board-container">');
                _$spa.append(_$container);
                SPA.GameModule.init(_$container, columns, grid);
                const fields = $(_$container).find('.reversi-field');
                $(fields).on('click', (ev) => {
                    let coordinates = $(ev.target).data();
                    makeMove(coordinates['col'], coordinates['row']);
                })
                subscribeToGameApi();
                $("#splash-container").css("display", "none");
            })
            .catch((err) => console.error(new Error(err)));

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
    let subscribeToGameApi = () => {
        SPA.ResponseModule.subscribe(_token, SPA.GameModule.updateGrid);
    }

    return {
        init : init
    }
})($);

