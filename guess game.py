import random
mynum = random.randint(1,100)
choice = 0
print('I HAVE A NUMBER IN MY MIND. CAN YOU GUESS IT?')
while True:
    usernum = int(input('ENTER THE GUESS'))
    if (choice == 5):
        print('GAME OVER')
        break   
    if (usernum > mynum):
        print('YOUR NUMBER IS BIG. TRY AGAIN')
    elif (usernum < mynum) :
        print('YOUR NUMBER IS SMALL. TRY AGAIN')
    else:
        print('CONGRATULATION!!! YOU WIN')
    choice += 1

      


