'''
1 for stone
-1 for paper
0 for scissor
'''

import random

computer= random.choice([-1, 0, 1])
youstr= input("Enter Your Choice:")
youDict={"stone":1,"saper":-1,"scissor":0}
reverseDict={1:"stone",-1:"paper",0:"scissor"}
you = youDict[youstr]

print(f"You Chose:{reverseDict[you]}\nComputer Chose:{reverseDict[computer]}")

if(computer==1 and you==1):
    print("Draw!")

elif(computer==1 and you==-1): #1--1=2
    print("You Win!")

elif(computer==1 and you==0):   #1-0=1
    print("You Loose")
elif(computer==-1 and you==1):  #-1-1=2
    print("You Loose")

elif(computer==-1 and you==-1):
    print("Draw!")

elif(computer==-1 and you==0):  #-1-0=-1
    print("You Win!")    

elif(computer==0 and you==1):   #0-1=-1
    print("You Win!")


elif(computer==0 and you==-1):
    print("You Loose")

elif(computer==0 and you==0):
    print("Draw!")

else:
    print("Something went wrong!")


