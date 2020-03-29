const SPA = (($) => {
    "use strict"

    let init;
    let _$spa, _$container, _token 

    init = (spa) => {
        _$spa = $(spa); 
        $("#game-toggle-open").on('click', () => {
            openReversiWindow();
        });
        
    }

    let openReversiWindow = () => {
        if (_$container == undefined){
            let tokenPromise = SPA.ResponseModule.getPlayerToken;
            let gamePromise = SPA.ResponseModule.joinGame;
    
            _$container = reversiBoardContainer();
            _$container.append(splashScreen());
            _$spa.append(_$container);
    
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
                    _$container.find('.section-header').append(data['playerColor'] == -1 ? ' (b)' : ' (w)');
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
                
            $("#game-toggle-close").on('click', closeReversiWindow);
        } else {
            _$container.css('display', 'inline-block');
        }
    }

    let closeReversiWindow = () => {
        if (_$container != undefined){
            _$container.css('display', 'none');
        }
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

    let splashScreen = () => { // TODO: handlebars van maken
        return $(
            `
                <div id="splash-container">
                    <div class="ring-wrapper">
                        <div class="outer ring">
                        </div>
                    </div>
                    <div class="ring-wrapper">
                        <div class="inner ring">
                        </div>
                    </div>
                    <div class="ring-wrapper">
                        <div class="middle ring">
                        </div>
                    </div>
                </div>
                `
        );
    }

    let reversiBoardContainer = () => { // TODO: handlebars van maken
        return $(
            `
                <div id="reversi-board-container">
                    <span class="close" id="game-toggle-close"></span>
                    <h3 class="section-header"> Reversi </h3>
                    
                </div>
            `);
    }

    return {
        init : init
    }
})($);

