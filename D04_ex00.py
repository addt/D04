#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports


# Body


def random():
 import random
 random_no = random.randrange(1,25,1)
 print("The random no is: "+str(random_no))
 count = 0

 while count < 5:
    try:
        user = int(input('Enter a number'))
        if user == random_no:
            print("Correct!!!!!")
            break
        elif user > random_no:
            print("Too High!")
            count = count + 1
        elif user < random_no:
            print("Too Low!")
            count = count + 1
    except:
        count = count + 1
        print("Enter a No")


################################################################################
def main():


    random()
    

if __name__ == '__main__':
    main()
