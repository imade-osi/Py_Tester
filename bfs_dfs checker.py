# // binaryMatrix: same as below
# // visited: 2d array, same size as binaryMatrix, true if we've already visited it

# /*
# 12345
# 12345
# 12345

# [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
# [item1, item2, item3]
# 5 cols, 3 rows
# item1: [1,2,3,4,5]
# arr.length = 3 -> rows
# arr[0].length = 5 -> cols
# */

# function dfs(binaryMatrix, col, row, visited) {
#   // if it's out of bounds, don't even try
#   if (row < 0 || col < 0 || col >= binaryMatrix[0].length || row >= binaryMatrix.length) {
#     return;
#   }
#   // if we've already visited, stop
#   if (visited[col][row]) {
#     return;
#   }
#   visited[col][row] = true;
#   if (binaryMatrix[col][row] === 0) {
#     return;
#   }// binaryMatrix: same as below
# // visited: 2d array, same size as binaryMatrix, true if we've already visited it

# /*
# 12345
# 12345
# 12345

# [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
# [item1, item2, item3]
# 5 cols, 3 rows
# item1: [1,2,3,4,5]
# arr.length = 3 -> rows
# arr[0].length = 5 -> cols
# */

# function dfs(binaryMatrix, col, row, visited) {
#   // if it's out of bounds, don't even try
#   if (row < 0 || col < 0 || col >= binaryMatrix[0].length || row >= binaryMatrix.length) {
#     return;
#   }
#   // if we've already visited, stop
#   if (visited[col][row]) {
#     return;
#   }
#   visited[col][row] = true;
#   if (binaryMatrix[col][row] === 0) {
#     return;
#   }
#   dfs(binaryMatrix, col, row-1, visited);
#   dfs(binaryMatrix, col+1, row, visited);
#   dfs(binaryMatrix, col, row+1, visited);
#   dfs(binaryMatrix, col-1, row, visited);
# }

# function getNumberOfIslands(binaryMatrix) {
#   var numberOfIslands = 0;
#   const numberOfCols = binaryMatrix[0].length;
#   const numberOfRows = binaryMatrix.length;
#   const visited = new Array(numberOfRows).fill(false).map(() => new Array(numberOfCols).fill(false));
#   for (var col = 0; col < numberOfCols; col++) {
#     for (var row = 0; row < numberOfRows; row++) {
#       if (binaryMatrix[col][row] === 1 && !visited[col][row]) {
#         numberOfIslands++;
#         dfs(binaryMatrix, col, row, visited);
#       }
#     }
#   }
#   return numberOfIslands;
# }

#   dfs(binaryMatrix, col, row-1, visited);
#   dfs(binaryMatrix, col+1, row, visited);
#   dfs(binaryMatrix, col, row+1, visited);
#   dfs(binaryMatrix, col-1, row, visited);
# }

# function getNumberOfIslands(binaryMatrix) {
#   var numberOfIslands = 0;
#   const numberOfCols = binaryMatrix[0].length;
#   const numberOfRows = binaryMatrix.length;
#   const visited = new Array(numberOfRows).fill(false).map(() => new Array(numberOfCols).fill(false));
#   for (var col = 0; col < numberOfCols; col++) {
#     for (var row = 0; row < numberOfRows; row++) {
#       if (binaryMatrix[col][row] === 1 && !visited[col][row]) {
#         numberOfIslands++;
#         dfs(binaryMatrix, col, row, visited);
#       }
#     }
#   }
#   return numberOfIslands;
# }
