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
    }

    let makeMove = (col, row) => {
        return new Promise((resolve, reject) => {
            var moveResponse = SPA.responseModule.move(col, row);

            Promise.all([moveResponse])
            .then(() => {
                console.log('move went through')
            })
            .catch(() => {
                alert('something went wrong.');
            });
        });
    }
    
    return {
        init : init
    }
})($);

