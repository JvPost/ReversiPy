let GameModule = (($) => {
    "use strict"

    let init, updateGrid;
    let _$container, _grid, _$board, _$rowInfo, _$colInfo, _playerColor

    init = ($container) => {
        _$container = $container
        _grid = {
            "A" : [],
            "B" : [],
            "C" : [],
            "D" : [],
            "E" : [],
            "F" : [],
            "G" : [],
            "H" : [],
        }
        
        _$rowInfo = $('<div id="row-info">');
        _$colInfo = $('<div id="col-info">');
        _$board = $('<div id="reversi-board">');
        _playerColor = 1 

        // loop rows
        for(let i = 0; i < 8; i++){
            let row = i+1;
            $(_$rowInfo).append('<div class="row-info-cell"> <span>'+ row.toString() +'</span> </div>');
            // loop cols to make fields
            for (const key in _grid) {
                if (_grid.hasOwnProperty(key)) {
                    let $field = $('<div data-row="'+ row +'" data-col="'+ key +'" data-played="0" class="reversi-field"></div>');
                    _grid[key].push($field);
                    $(_$board).append($field);
                }
            }
        }

        // loop cols
        for (const key in _grid) {
            if (_grid.hasOwnProperty(key)) {
                $(_$colInfo).append('<div class="col-info-cell">'+ key +'</div>')
            }
        }

        $(_$container).append(_$rowInfo);
        $(_$container).append(_$board);
        $(_$container).append(_$colInfo);
    }
    
    updateGrid = (row, col) => {
        let field = _grid[col][row - 1];
        $(field).attr("data-played", _playerColor);
        field.append(fiche());
    }

    let fiche = () => {
        return $('<div class="fiche"></div>');
    }

    return {
        init: init,
        updateGrid: updateGrid
    } 
})($);