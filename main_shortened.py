

import random

computer= random.choice([-1, 0, 1])
youstr= input("Enter Your Choice:")
youDict={"stone":1,"paper":-1,"scissor":0}
reverseDict={1:"stone",-1:"paper",0:"scissor"}
you = youDict[youstr]

print(f"You Chose:{reverseDict[you]}\nComputer Chose:{reverseDict[computer]}")


# 1 for stone
#-1 for paper
# 0 for scissor

#logic,if computer-you= 2 or -1 then you win

if(computer==you):
    print("Its a Draw!")
else:
    if(computer-you==-1 or computer-you==2):
        print("You Win!")
    else:
        print("You loose")
