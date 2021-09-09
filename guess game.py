import random
mynum = random.randint(1,100)
ch = 'y'
choice = 0
print('I HAVE A NUMBER IN MY MIND. CAN YOU GUESS IT?')
while True:
    usernum = int(input('ENTER THE GUESS'))
    if (choice == 10):
        print('GAME OVER')
        break   
    if (usernum > mynum):
        print('YOUR NUMBER IS BIG. TRY AGAIN')
    elif (usernum < mynum) :
        print('YOUR NUMBER IS SMALL. TRY AGAIN')
    else:
        print('CONGRATULATION!!! YOU WIN')
        ch = input('Press y to continue the game')
    choice += 1

    

    

      


