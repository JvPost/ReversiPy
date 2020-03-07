const SPA = (($) => {
    let init;

    init = (spaID) => {
        $spa = $("#" + spaID); 
        $container = $('<div id="reversi-board-container">')
        $spa.append($container)
        SPA.gameModule.init($container);

        const fields = $($container).find('.reversi-field');
        $(fields).on('click', (ev) => {
            let data = $(ev.target).data();
            makeMove(data['col'], data['row']);
        });

        // test btn
        let btn = $('<input type="button" value="log data from test game" >');
        $(btn).on('click', function(){
            getGameInfo(0);
        });
        $($spa).append(btn);
    }

    let makeMove = (col, row) => {
        return new Promise((resolve, reject) => {
            let moveResponse = SPA.responseModule.move(0, col, row);
            Promise.all([moveResponse])
            .then(() => {
                SPA.gameModule.updateGrid(row, col);
                
            })
            .catch(() => {
                alert('something went wrong.');
            });
        });
    }

    let getGameInfo = (token) => {
        return new Promise((resolve, reject) => {
            let gameInfoPromise = SPA.responseModule.getGameInfo(token);
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

