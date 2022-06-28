from operator import truediv
from random import randint
turnCount = 0

spacesArray = [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', True]

grid = f"""
     1 | 2 | 3 
     {spacesArray[0]} | {spacesArray[1]} | {spacesArray[2]} 
       |   |   
    -----------
     4 | 5 | 6 
     {spacesArray[3]} | {spacesArray[4]} | {spacesArray[5]} 
       |   |   
    -----------
     7 | 8 | 9 
     {spacesArray[6]} | {spacesArray[7]} | {spacesArray[8]} 
       |   |   
    """

# define functions to update grid
def updateGrid():
    grid = f"""
    1 | 2 | 3 
    {spacesArray[0]} | {spacesArray[1]} | {spacesArray[2]} 
        |   |   
    -----------
    4 | 5 | 6 
    {spacesArray[3]} | {spacesArray[4]} | {spacesArray[5]} 
        |   |   
    -----------
    7 | 8 | 9 
    {spacesArray[6]} | {spacesArray[7]} | {spacesArray[8]} 
        |   |   
    """

def playerTurn(arrayIndex):
    spacesArray[arrayIndex] = 'X'

    grid = f"""
    1 | 2 | 3 
    {spacesArray[0]} | {spacesArray[1]} | {spacesArray[2]} 
      |   |   
    -----------
    4 | 5 | 6 
    {spacesArray[3]} | {spacesArray[4]} | {spacesArray[5]} 
      |   |   
    -----------
    7 | 8 | 9 
    {spacesArray[6]} | {spacesArray[7]} | {spacesArray[8]} 
      |   |   
    """

    print(spacesArray)
    print(grid)

def computerTurn(arrayIndex):
    spacesArray[arrayIndex] = 'O'

    grid = f"""
    1 | 2 | 3 
    {spacesArray[0]} | {spacesArray[1]} | {spacesArray[2]} 
      |   |   
    -----------
    4 | 5 | 6 
    {spacesArray[3]} | {spacesArray[4]} | {spacesArray[5]} 
      |   |   
    -----------
    7 | 8 | 9 
    {spacesArray[6]} | {spacesArray[7]} | {spacesArray[8]} 
      |   |   
    """

    print(spacesArray)
    print(grid)

def checkWinConditions():
  #Horizontals
  if spacesArray[0] != ' ' and spacesArray[0] == spacesArray[1] and spacesArray[0] == spacesArray[2]:
    winner = spacesArray[0]
    print(f'{winner}\'s are the winners')
    spacesArray[9] = False
  elif spacesArray[3] != ' ' and spacesArray[3] == spacesArray[4] and spacesArray[3] == spacesArray[5]:
    winner = spacesArray[3]
    print(f'{winner}\'s are the winners')
    spacesArray[9] = False
  elif spacesArray[6] != ' ' and spacesArray[6] == spacesArray[7] and spacesArray[6] == spacesArray[8]:
    winner = spacesArray[6]
    print(f'{winner}\'s are the winners')
    spacesArray[9] = False
  #Diagonals
  elif spacesArray[0] != ' ' and spacesArray[0] == spacesArray[4] and spacesArray[0] == spacesArray[8]:
    winner = spacesArray[0]
    print(f'{winner}\'s are the winners')
    spacesArray[9] = False
  elif spacesArray[6] != ' ' and spacesArray[6] == spacesArray[4] and spacesArray[6] == spacesArray[2]:
    winner = spacesArray[6]
    print(f'{winner}\'s are the winners')
    spacesArray[9] = False
  #Vertical line wins
  elif spacesArray[0] != ' ' and spacesArray[0] == spacesArray[3] and spacesArray[0] == spacesArray[6]:
    winner = spacesArray[0]
    print(f'{winner}\'s are the winners')
    spacesArray[9] = False
  elif spacesArray[1] != ' ' and spacesArray[1] == spacesArray[4] and spacesArray[1] == spacesArray[7]:
    winner = spacesArray[1]
    print(f'{winner}\'s are the winners')
    spacesArray[9] = False
  elif spacesArray[2] != ' ' and spacesArray[2] == spacesArray[5] and spacesArray[2] == spacesArray[8]:
    winner = spacesArray[2]
    print(f'{winner}\'s are the winners')
    spacesArray[9] = False


##Draw initial game grid

print(grid)

print('__________________________')
print('Crosses (x) goes first')

while spacesArray[9] == True:
    playerChoice = input('Pick a space(1 - 9): ')
    spaceIndex = (int(playerChoice)-1)
    playerTurn(spaceIndex)
    turnCount += 1
    if turnCount == 9:
      print('Looks like nobody won today!')
      spacesArray[9] = False
    compRandom = randint(0, 8)
    while spacesArray[compRandom] != ' ':
        compRandom = randint(0, 8)
    computerTurn(compRandom)
    turnCount += 1
    checkWinConditions()
    if spacesArray[9] == False:
      print('Thanks for playing')

