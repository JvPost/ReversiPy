SPA.responseModule = (($) => {
    let move;
    let _path = "http://localhost:5001";
    
    // token, row, col
    move = (token, col, row) => {
        return new Promise((resolve, reject) => {
            $.ajax(_path + '/api/Spel/Zet',
            {
                method: 'PUT',
                data: { 
                    col: col,
                    row: row,
                    token: '', // TODO: get and use
                    moveType // set and use
                },
                dataType: 'JSON',
                success: (data) => {
                    resolve(data);
                },
                failed: (data) => {
                    reject('failed');
                }
            });
        });
    }
    
    return {
        move : move
    };
})($);