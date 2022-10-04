import datetime
import os
from turtle import st
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
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
def generate_receipt():
    doc = SimpleDocTemplate("receipt.pdf", pagesize=A4)
    elements = []
    data = [
        ["Surname", "Adult", "Child", "Senior", "Wristband", "Parking", "Total"],
        [surname_for_booking, adult_tickets, child_tickets, senior_tickets, wristband_tickets, parking_pass, total]
    ]
    t = Table(data)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ]
    ))
    elements.append(t)
    doc.build(elements)
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
    print("Your tickets will be printed now\n")
    generate_receipt()
    print("Your receipt is in 'receipt.pdf'")