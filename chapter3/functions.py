import sys

def collatz(number):
  if number % 2 == 0:
    return number // 2
  else:
    return (3 * number) + 1

def userInput():
  print('Enter a value');
  examination = int(input());
  while examination != 1:
    examination = collatz(examination)
    print(examination)
  sys.exit();

userInput()
