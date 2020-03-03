SPA.responseModule = (($) => {
    let move;
    let _path = "http://localhost:5001";
    
    // token, row, col
    move = (moveType, col, row) => {
        
        return new Promise((resolve, reject) => {
            $.ajax(_path + '/api/Spel/Zet',
            {
                method: 'PUT',
                dataType: 'JSON',
                data: JSON.stringify({ 
                    moveType: moveType,
                    col: col,
                    row: row
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
    
    return {
        move : move
    };
})($);