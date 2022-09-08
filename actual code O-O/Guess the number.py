from random import randint
testing = False
if testing == False:
    number = randint(1,10)
else:
    number = 5
guesses = 3
print("Guess a number between 1 and 10")
guess = int(input())
while guess != number:
    guesses -= 1
    if guesses == 0:
        print("You lose")
        exit()
    print("Incorrect")
    print("Guess a number between 1 and 10")
    guess = int(input())
print("Correct")
print(f"You finished with {guesses} guesses left")