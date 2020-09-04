import random

winner = True
tie = False
options = ["Rock", "Paper", "Scissors"]
#Title Screen

# Give them instructions



#Ask the user name
name  = input("what's your name\n")  

while tie == False:
  # USER SELECTION
  user_answer = options[int(input("\nHi " + name + " What would you like to choose?\nWrite the NUMBER OF YOUR CHOICE\n\n(0)Rock\n(1)Paper\n(2)Scissors\n\n"))]
  #CPU SELECTION
  cpu = options[random.randint(0,2)]
  if user_answer == cpu:
    tie = True
    print ("WE HAVE A TIE")
    print("CPU chose =", cpu,"AND YOU CHOSE =",user_answer)
    print ("TRY AGAIN\n")



# 1=Rock 2=Paper 3=Scissors
#THIS IS THE USER CHOICE
if user_answer == options[0] :
  if cpu == options[1]:
   print("CPU", cpu,"covers your",user_answer)
   winner = False
elif user_answer == options[1]:
  if cpu == options[2]:
    print("CPU", cpu,"cuts your",user_answer)
    winner = False
elif user_answer == options[2]:
  if cpu == options[0]:
    print("CPU", cpu,"smashes your",user_answer)
    winner = False
else:
  print ("choose something idiot \n ONLY CHOOSE FROM \n\n ROCK PAPER SCISSORS")

#THIS IS THE WIN / TIE CHECK
if user_answer != cpu:
  if winner == False:
    print ("YOU LOSE")
    print("CPU chose =", cpu,"AND YOU CHOSE =",user_answer)
  else:
    print ("YOU WIN")
    print("CPU chose =", cpu,"AND YOU CHOSE =",user_answer)
else:
  tie = True
  print ("WE HAVE A TIE")
  print("CPU chose =", cpu,"AND YOU CHOSE =",user_answer)


#THIS IS THE  CPU WIN CHECK


#print(name + " WINS!!!!")


#THIS IS FOR DEBUGGING 
print("\n\n### THIS IS ONLY FOR DEBUGGING ###")
print(name)
print(user_answer)
print(cpu)
print(winner)


#Print a response depending