def commaCode(needsChanging):
  returnString = ''
  for i in range(len(needsChanging)):
    if i != len(needsChanging) - 1:
      returnString += needsChanging[i] + ', '
    else:
      returnString += needsChanging[i]
  return returnString


print(commaCode(['apples', 'bananas', 'tofu', 'cats']))
