to_guess = 4
number = 0
not_guessed = to_guess != number

while not_guessed:
    print("Guess a number between 1 and 10")
    try:
        number = int(input())
    except:
        print("top 10 anime betrayals")
    if number < 1 or number > 10:
        print("Number out of range")
    elif number == to_guess:
        not_guessed = False
print("You got it!")