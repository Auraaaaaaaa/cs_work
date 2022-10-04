import datetime
import os
def clear():
   if os.name == 'posix' or 'Darwin':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
print("Welcome to the ticketing system of doom that i was asked to make")
print("Here are the enterance ticket prices:\nAdult: £20\nChild: £10\nSenior: £11\nWristband: £20\nParking: Free")
adult_tickets = int(input("How many adult tickets would you like to buy? "))
child_tickets = int(input("How many child tickets would you like to buy? "))
senior_tickets = int(input("How many senior tickets would you like to buy? "))
wristband_tickets = int(input("How many wristband tickets would you like to buy? "))
if (input("Do you need a parking pass? (y/n) ").lower == "y"):
    parking_pass = True
else:
    parking_pass = False
total = (adult_tickets * 20) + (child_tickets * 10) + (senior_tickets * 11) + (wristband_tickets * 20)
surname_for_booking = input("What is your surname for the booking? ")
clear()
print("Please pay the cashier")
print("Your total is £" + str(total))
print("I am afraid that you need to pay with cash, in £10 or £20 notes")
notes_10 = int(input("How many £10 notes do you have? "))
notes_20 = int(input("How many £20 notes do you have? "))
if (notes_10 * 10) + (notes_20 * 20) < total:
    print("You do not have enough money")
    exit(0)
else:
    clear()
    print("Thank you for your payment")
    print("Here is your receipt")
    print("Surname: " + surname_for_booking)
    print("Adult tickets: " + str(adult_tickets))
    print("Child tickets: " + str(child_tickets))
    print("Senior tickets: " + str(senior_tickets))
    print("Wristband tickets: " + str(wristband_tickets))
    print("Parking pass: " + str(parking_pass))
    print("Total: £" + str(total))
    print("Change: £" + str((notes_10 * 10) + (notes_20 * 20) - total))
    print("Have a nice day!")
    print("Your tickets (and parking pass) will be printed now\n")
    print("+------------------------+")
    print("Name: " + surname_for_booking)
    print("Adult tickets: " + str(adult_tickets))
    print("Child tickets: " + str(child_tickets))
    print("Senior tickets: " + str(senior_tickets))
    print("Wristband tickets: " + str(wristband_tickets))
    print("Total: £" + str(total))
    print("Day of purchase: " + str(datetime.datetime.now()))
    print("+------------------------+")
    print("Parking pass:")
    print("+------------------------+")
    print("Parking Pass")
    print("Name: " + surname_for_booking)
    print("Day of purchase: " + str(datetime.datetime.now()))
    print("+------------------------+")