shopping = []
if input("Would you like to edit your shopping list?").upper == "YES":
    while True:
        item = input("What would you like to add to your shopping list?")
        shopping.append(item)
        if input("Would you like to add another item?").upper == "NO":
            break
while True:
    print("Your shopping list is: " + str(shopping))
    if input("Would you like to remove an item?").upper == "YES":
        item = input("What item would you like to remove?")
        shopping.remove(item)
    elif input("Would you like to add an item?").upper == "YES":
        item = input("What item would you like to add?")
        shopping.append(item)