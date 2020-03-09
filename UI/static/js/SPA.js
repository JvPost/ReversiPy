const SPA = (($) => {
    "use strict"

    let init;
    let _$spa, _$container, _token 

    init = (spa) => {
        _$spa = $(spa); 
        _$container = $('<div id="reversi-board-container">')
        _$spa.append(_$container)
        GameModule.init(_$container);
        ResponseModule.init();

        // move event handlers
        const fields = $(_$container).find('.reversi-field');
        $(fields).on('click', (ev) => {
            let data = $(ev.target).data();
            makeMove(data['col'], data['row']);
        });

        // game info button
        let btn = $('<input type="button" value="log data from test game" >');
        $(btn).on('click', function(){
            getGameInfo(0);
        });

        let surrenderBtn = $('<input type="button" value="Surrender"');
        $(surrenderBtn).on('click', () => {

        });

        _$spa.append(btn);
    }

    let makeMove = (col, row) => {
        return new Promise((resolve, reject) => {
            ResponseModule.move(0, col, row)
            .then(() => {
                GameModule.updateGrid(row, col);
            })
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

    let surrender = (token) => {
        return new Promise((resolve, reject) => {
            let surrenderPromise = ResponseModule.surrender(token);
            
        })
    }
    
    return {
        init : init
    }
})($);

