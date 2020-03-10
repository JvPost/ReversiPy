let GameModule = (($) => {
    "use strict"

    let init, updateGrid;
    let _$container, _grid, _$board, _$rowInfo, _$colInfo, _playerColor

    init = ($container, grid) => {
        _$container = $container
        _grid = grid
        
        _$rowInfo = $('<div id="row-info">');
        _$colInfo = $('<div id="col-info">');
        _$board = $('<div id="reversi-board">');
        _playerColor = 1 

        let letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        for (let i = 0; i < letters.length; i++){
            let row = _grid[letters[i]];
            let rowIndicator = i+1;
            $(_$rowInfo).append('<div class="row-info-cell"> <span>'+ rowIndicator +'</span> </div>');
            for (let j = 0; j < row.length; j++){
                let key = letters[j];
                let playedBy = row[j];
                let $field = $('<div data-row="'+ rowIndicator +'" data-col="'+ key +'" data-played=' + playedBy + ' class="reversi-field"></div>');
                if (playedBy != 0){
                    $field.append(fiche());
                }
                $(_$board).append($field);
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
    
    updateGrid = (row, col, playerColor) => {
        let fields = $('.reversi-field');
        let start = (row-1) * 8;
        let end = start + 8;
        for( let i = start; i<end; i++){
            console.log(i)
            if ($(fields[i]).attr('data-col') == col){
                $(fields[i]).attr("data-played", playerColor);
                $(fields[i]).append(fiche());
                break;
            }
        }
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