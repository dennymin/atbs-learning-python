# we are going to use the same code from the previous project to detect whether the user types in a noninteger string. Normally, the int() function will raise a ValueError error if it is passed a noninteger string. In the except clause, print a message to the user saying they must enter an integer.

import sys


def collatz(number):
  if number % 2 == 0:
    return number // 2
  else:
    return (3 * number) + 1


def userInput():
  print('Enter a value')
  try:
    examination = int(input())
  except:
    print('Error: needs an integer!')
  while examination != 1:
    examination = collatz(examination)
    print(examination)
  sys.exit()


userInput()
