function searchMatrix(matrix: number[][], target: number): boolean {
    var m:number = matrix.length;
    var n:number = matrix[0].length;
    for (let i = 0; i < m; i ++){
        for (let j = 0; j < n; j ++){
            if (matrix[i][j] == target){
                return true
            };
        };
    };
    return false
};