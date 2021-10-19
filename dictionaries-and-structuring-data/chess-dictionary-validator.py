def boardGenerator(board):
  alphas = ['a','b','c','d','e','f','g','h']
  nums = range(1, 8)
  fullSet = []
  for i in range(len(nums)):
    for j in range(len(alphas)):
      spot = str(nums[i]) + alphas[j]
      fullSet.append(spot)

  units = ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']
  teams = ['b', 'w']
  fullTeam = []
  for i in range(len(teams)):
    for j in range(len(units)):
      armed = teams[i] + units[j]
      fullTeam.append(armed)

  for i in board.keys():
    if i not in fullSet:
      return False

  tempBoard = []
  blackPawnCounter = 0
  whitePawnCounter = 0
  for i in board.values():
    if i not in fullTeam or (i in tempBoard and i != 'bpawn' and i != 'wpawn'):
      return False
    tempBoard.append(i)
    if i == 'bpawn':
      blackPawnCounter += 1
    if i == 'wpawn':
      whitePawnCounter += 1

  if blackPawnCounter > 7 or whitePawnCounter > 7:
    return False


  return True


print(boardGenerator({'1h': 'bking', '6c': 'wqueen',
      '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
