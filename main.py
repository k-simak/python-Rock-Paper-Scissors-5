import random

winner = True
#Title Screen

# Give them instructions



#Ask the user name
name  = input("what's your name\n")  
user_answer = int(input("\nHi " + name + " What would you like to choose?\nWrite the NUMBER OF YOUR CHOICE\n\n(1)rock\n(2)paper\n(3)scissors\n\n"))

#CPU choses at the same time as player
cpu = random.randint(1,3)


# 1=Rock 2=Paper 3=Scissors
#THIS IS THE USER CHOICE
if user_answer == 1:
  print ("\nYou choose ROCK")
  #print ("The CPU chose {}" .format(cpu))
  if cpu == 2:
    print("CPU paper covers your ROCK")
    winner = False
elif user_answer == 2:
  print ("You choose PAPER")
elif user_answer == 3:
  print ("You choose SCISSORS")
else:
  print ("choose something idiot \n ONLY CHOOSE FROM \n\n ROCK PAPER SCISSORS")

#THIS IS THE TIE CHECK
if user_answer == cpu:
  tie = True
  print ("\n\nWE HAVE A TIE!!!!!\n\n")



#THIS IS THE  CPU WIN CHECK
if winner == False:
  print("\nYOU LOSE\n")
else:
  print("\nYOU ARE THE WINNER!!\n")

#print(name + " WINS!!!!")






#THIS IS FOR DEBUGGING 
print("\n\n\n### THIS IS ONLY FOR DEBUGGING ###")
print(name)
print(user_answer)
print(cpu)
print(winner)


#Print a response depending