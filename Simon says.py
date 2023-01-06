from random import choice
def get_choices():
    print("Enter a choice for Simon to say, or DONE to stop")
    choices = []
    while True:
        choice = input()
        if choice == "DONE":
            return choices

        choices.append(choice)

simon_says = get_choices();
intros = ["Simon says...", ""]

print ("Pick a number between 0 and " + str(len(simon_says) - 1))
while (True):
    intro = choice(intros)
    index = int(input())
    instruction = simon_says[index]
    print(intro + instruction)