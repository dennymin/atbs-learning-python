grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
def printRegGrid(shape):
  for i in range(len(shape)):
    print(shape[i])
printRegGrid(grid)

def flipGrid(shape):
  newGrid = []
  for i in range(len(shape[0])):
    newRow = []
    for j in range(len(shape)):
      newRow.append(shape[j][i])
    newGrid.append(newRow)
    print(newRow)
  return newGrid
flipGrid(grid)
