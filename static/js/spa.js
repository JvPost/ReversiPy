const SPA = (($) => {
    "use strict"

    let init;
    let _$spa, _$container

    init = (spaID) => {
        _$spa = $("#" + spaID); 
        _$container = $('<div id="reversi-board-container">')
        _$spa.append(_$container)
        gameModule.init(_$container);

        const fields = $(_$container).find('.reversi-field');
        $(fields).on('click', (ev) => {
            let data = $(ev.target).data();
            makeMove(data['col'], data['row']);
        });

        // test btn
        let btn = $('<input type="button" value="log data from test game" >');
        $(btn).on('click', function(){
            getGameInfo(0);
        });
        $(_$spa).append(btn);
    }

    let makeMove = (col, row) => {
        return new Promise((resolve, reject) => {
            let moveResponse = responseModule.move(0, col, row);
            Promise.all([moveResponse])
            .then(() => {
                gameModule.updateGrid(row, col);
            })
            .catch(() => {
                alert('something went wrong.');
            });
        });
    }

    let getGameInfo = (token) => {
        return new Promise((resolve, reject) => {
            let gameInfoPromise = responseModule.getGameInfo(token);
            Promise.all([gameInfoPromise])
            .then((gameInfo) => {
                console.log(gameInfo)
            })
            .catch(() => {
                alert('something went wrong')
            });
        });
    }
    
    return {
        init : init
    }
})($);

