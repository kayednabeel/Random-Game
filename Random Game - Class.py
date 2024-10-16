import random


class RandomGame:
    def __init__(self, low, high):
        self.random_number = random.randint(low, high)
        self.low = low
        self.high = high

    def generate_random(self, low, high):
        self.random_number = random.randint(low, high)

    def play_game(self):
        self.generate_random(self.low, self.high)
        print("We have a random number between 1 and 100 please try to guess it, We will help you with hints until you "
              "find the correct one")

        while True:
            guessed_number = input()
            if not guessed_number.isnumeric():
                print("Please enter a valid integer")
                continue
            else:
                guessed_number = int(guessed_number)

            if guessed_number == self.random_number:
                print("Your answer is correct")
                break
            elif guessed_number > self.random_number:
                print("Your answer is greater than the correct number")
            else:
                print("Your answer is less than the correct number")


rand = RandomGame(1, 100)
rand.play_game()
