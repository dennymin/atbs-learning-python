def printTable(stringData):
  colWidth = [0] * len(stringData)
  for i in range(len(stringData)):
    for j in range(len(stringData[i])):
      if len(stringData[i][j]) > colWidth[i]:
        colWidth[i] = len(stringData[i][j])

  for i in range(len(stringData)):
    colMaxLength = colWidth[i]
    for j in range(len(stringData[i])):
      stringData[i][j] = stringData[i][j].rjust(colMaxLength)

  stringResult = ''
  for i in range(len(stringData[0])):
    row = ''
    for j in range(len(stringData)):
      if j != len(stringData[j]):
        row = row + stringData[j][i] + ' '
      else:
        row = row + stringData[j][i]
    row += '\n'
    stringResult += row
  return stringResult



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print(printTable(tableData))
