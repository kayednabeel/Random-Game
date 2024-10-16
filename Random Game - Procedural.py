import random

random_number = random.randint(1, 100)
print("We have a random number between 1 and 100 please try to guess it, We will help you with hints until you find "
      "the correct one")

while True:
    guessed_number = int(input())
    if guessed_number == random_number:
        print("Your answer Correct")
        break
    elif guessed_number > random_number:
        print("Your answer is greater than the correct number")
    else:
        print("Your answer is less than the correct number")
