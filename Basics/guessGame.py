import random

randomnum = random.randint(1,100)

while True:
    num= int(input("Enter guessed number: "))
    if randomnum>num:
        print ("You guessed the Wrong Number, Go for greater one..")
    elif randomnum<num:
        print ("You guessed the Wrong Number, Go for smaller one.")
    else:
        print(f"You guess the right number. i.e: {num} ")
        break

