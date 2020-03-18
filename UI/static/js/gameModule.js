let GameModule = (($) => {
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