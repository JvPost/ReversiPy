const SPA = (($) => {
    "use strict"

    let init;
    let _$spa, _$container, _token 

    init = (spa) => {
        _$spa = $(spa); 
        $(".game-toggle").on('click', () => {
            openReversiWindow();
        });
    }

    let openReversiWindow = () => {
        if (_$container == undefined){
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
                    // $('#Title').append(data['playerColor'] == -1 ? ' (b)' : ' (w)');
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
        } else if (_$container.css('display') == 'inline') {
            _$container.css('display', 'none');
        } else {
            _$container.css('display', 'inline');
        }

        let tokenPromise = SPA.ResponseModule.getPlayerToken;
        let gamePromise = SPA.ResponseModule.joinGame;

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
                    <a href="#" class="close game-toggle"></a>
                    <h3 class="section-header"> Reversi </h3>
                </div>
            `);
    }

    return {
        init : init
    }
})($);


SPA.GameModule = (($) => {
    "use strict"

    let init, updateGrid;
    let _$container, _$grid = [], _grid, _$board, _$rowInfo, _$colInfo, _playerColor, _columns
    
    init = ($container, columns, grid) => {
        // vars
        _columns = columns;
        _grid = grid
        
        // elements
        _$container = $container;
        for (let i = 0; i < _grid.length; i++) {
            _$grid.push([])
        }


        _$rowInfo = $('<div id="row-info">');
        _$colInfo = $('<div id="col-info">');
        _$board = $('<div id="reversi-board">');

        _grid.forEach((row, i) => {
            const rowNr = i+1;
            $(_$rowInfo).append('<div class="row-info-cell"> <span>' + rowNr + '</span> </div>');
            row.forEach((field, j) => {
                const col = _columns[j];
                const playedBy = _grid[i][j];
                const $field = $('<div data-row="'+ rowNr +'" data-col="'+ col +'" data-played=' + playedBy + ' class="reversi-field"></div>');
                if (playedBy != 0){
                    $field.append(fiche());
                }
                _$grid[i].push($field);
                $(_$board).append($field);
            });
        });

        _columns.forEach(col => {
            $(_$colInfo).append('<div class="col-info-cell">'+ col + '</div>');
        });

        $(_$container).append(_$rowInfo);
        $(_$container).append(_$board);
        $(_$container).append(_$colInfo);
    }
    
    updateGrid = (newGrid) => {
        let r = 0;
        newGrid.forEach(row => {
            let f = 0;
            row.forEach(field => {
                const newValue = field;
                const oldValue = _grid[r][f]
                if (newValue != oldValue){
                    if (oldValue == 0){
                        _$grid[r][f].append(fiche())
                    }   
                    _$grid[r][f].attr("data-played", newValue);
                }
                f++;
            });
            r++;
        });

        _grid = newGrid;
    }

    let fiche = () => {
        return $('<div class="fiche"></div>');
    }

    
    
    return {
        init: init,
        updateGrid: updateGrid,
        test: () => { console.log('test'); }
    } 
})($);
SPA.ResponseModule = (($) => {
    "use strict"

    let move, getGameInfo, getPlayerToken, joinGame, subscribe;
    let _path = "http://localhost:5001";
    

    // movetype, row, col
    move = (moveType, col, row, playerToken) => {
        return new Promise((resolve, reject) => {
            return $.ajax({
                url: _path + '/api/Spel/Zet',
                method: 'PUT',
                data: JSON.stringify({ 
                    moveType: moveType,
                    col: col,
                    row: row,
                    playerToken: playerToken
                    // TODO: Add game token
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
            return $.ajax(_path + '/api/Spel/' + token, {
                success: (data) => {
                    resolve(data);
                },
                failed: (data) => {
                    reject('failed');
                }
            });
        });
    }

    /**
     * Returns promise token for a player token. When the promise succeeds a token is returned, else 'failed' is returned.
     */
    getPlayerToken = () => {
        return new Promise((resolve, reject) => {
            return $.ajax(_path + '/api/Spel/GetPlayerToken',
                {
                    method: 'GET',
                    success: (data) => {
                        resolve(data);
                    },
                    failed: (err) => {
                        reject('failed'); // TODO: add search for game?
                    }
                });
        });
    }

    joinGame = (playerToken) => {
        return new Promise((resolve, reject) => {
            return $.ajax(_path + '/api/Spel/JoinGame/'+playerToken,
                {
                method: 'GET',
                success: (data) => {
                    resolve(data);
                },
                failed: (err) => {
                    reject('failed');
                }
            });
        });
    }

    subscribe = (playerToken, callback) => {
        var source = new EventSource(_path + '/api/Spel/Event/' + playerToken);
        source.onmessage = (event) => {
            if (event.data != "1"){
                let eventStr = event.data.split("'")[1];
                let eventJson = JSON.parse(eventStr);
                callback(eventJson)
            }
        }
    }
    
    return {
        move : move,
        getGameInfo: getGameInfo,
        getPlayerToken : getPlayerToken,
        joinGame: joinGame,
        subscribe: subscribe
    };
})($);