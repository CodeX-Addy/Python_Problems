import random #importing the random module
 
#initializing the variables
choices = ('r', 'p', 's')
cPoints = 0
pPoints = 0
 
def player():
   
  '''This function is used to get players choice.'''
   
  global choices #declaring the variable choices to be global
  symbol = input("Choose either rock(r), paper(p), or scissors(s). ").lower()
   
   
  if symbol not in choices:
    print("You did not enter a valid option. ")
    return player() #using recursion to get a valid input
  else:
    return symbol#if valid input return the answer
 
def computer():
 
  '''This function is used to get computers choice'''\
   
  return random.choice(choices)
 
def game():
 
  '''This function is used to play a single round of game'''
   
  global cPoints, pPoints #declaring cPoints and pPoints to be global
  pChoice = player()#getting the players choice
  cChoice = computer()#getting the computers choice
  print("The computer has chosen", cChoice)
  print("You chose", pChoice)
  if pChoice == cChoice: #checking for tie
    print("Its a tie! No one gets a point. ")
  elif (pChoice == "r" and cChoice == "s") or (pChoice == "s" and cChoice == "p") or (pChoice == "p" and cChoice == "r"): #checking if player scores a point
     
    print("You won! ")
    pPoints += 1 #increment the players point by 1
  else: #checking if computer scores a point
    print("Aww. I won. ")
    cPoints += 1 #increment the computer point by 1
  print()
 
print("Welcome to Rock Paper and Scissors game!!!")
while True: #creating an infinite loop
  for i in range(5):#loop that runs 5 times
    game() #calling the game for every single round
  print("Good job!\nYour score is:", pPoints, "\nMy score is", cPoints) #displaying the result after 5 rounds
  print()
  again = int(input("Press 1 to continue\nPress2 to reset and continue\npress 3 to exit "))
  if again==1: #this is executed if the user wants to play another 5 rounds
    continue
  elif again==2: #this is executed if the user wants to reset the scores and play another 5 rounds
    pPoints=0
    cPoints=0
    continue
  else: #this is executed if the user wants to quit.
    break
     
print("Ok! Bye!")
