import random

winner = True
options = ["Rock", "Paper", "Scissors"]
#Title Screen

# Give them instructions



#Ask the user name
name  = input("what's your name\n")  
user_answer = options[int(input("\nHi " + name + " What would you like to choose?\nWrite the NUMBER OF YOUR CHOICE\n\n(0)rock\n(1)paper\n(2)scissors\n\n"))]

#CPU choses at the same time as player
      #OLD CODE cpu = random.randint(1,3)
cpu = options[random.randint(0,2)]

# 1=Rock 2=Paper 3=Scissors
#THIS IS THE USER CHOICE
if user_answer == 1:
  print ("\nYou choose ROCK")
  #print ("The CPU chose {}" .format(cpu))
  if cpu == options[1]:
    print("CPU paper covers your ROCK")
    winner = False
elif user_answer == 2:
  print ("You choose PAPER")
  if cpu == 3:
    print("CPU scissors cuts your PAPER")
    winner = False
elif user_answer == 3:
  print ("You choose SCISSORS")
  if cpu == 1:
    print("CPU rock smashes your SCISSORS")
    winner = False
else:
  print ("choose something idiot \n ONLY CHOOSE FROM \n\n ROCK PAPER SCISSORS")

#THIS IS THE WIN / TIE CHECK
if user_answer != cpu:
  if winner == False:
    print ("YOU LOSE")
  else:
    print ("YOU WIN")
else:
  tie = True
  print ("WE HAVE A TIE")



#THIS IS THE  CPU WIN CHECK


#print(name + " WINS!!!!")






#THIS IS FOR DEBUGGING 
print("\n\n### THIS IS ONLY FOR DEBUGGING ###")
print(name)
print(user_answer)
print(cpu)
print(winner)


#Print a response depending