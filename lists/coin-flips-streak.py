import random
numberOfStreaks = 0
def streakGenerator():
  streak = []
  for experimentNumber in range(20):
      # Code that creates a list of 100 'heads' or 'tails' values.
    randomNumber = random.randint(0,1)
    if randomNumber == 1:
      streak.append('H')
    else:
      streak.append('T')
      # Code that checks if there is a streak of 6 heads or tails in a row.
  return streak

def streakFinder(array):
  counter = 0
  for i in range(len(array)-7):
    if array[i] == array[i+1] and array[i] == array[i+2] and array[i] == array[i+3] and array[i] == array[i+4] and array[i] == array[i+5]:
      counter += 1
  print(array)
  print('Chance of streak: %s%%' % (counter / 100))
  print(counter)
  return counter

testFunc = streakGenerator()
streakFinder(testFunc)
