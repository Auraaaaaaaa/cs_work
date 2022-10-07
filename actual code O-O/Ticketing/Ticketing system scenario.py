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
clear()
print("Welcome to the ticketing system of doom that i was asked to make")
print("Here are the enterance ticket prices:\nAdult: £20\nChild: £10\nSenior: £11\nWristband: £20\nParking: Free")
try:
    adult_total = int(input("How many adult tickets would you like to buy? "))
    child_total = int(input("How many child tickets would you like to buy? "))
    senior_total = int(input("How many senior tickets would you like to buy? "))
    wrist_total = int(input("How many wristband tickets would you like to buy? "))
except ValueError as e:
    print("Please enter a valid number")
    exit()
if (input("Do you need a parking pass? (Y/N) ").upper == "Y"):
    parking = True
else:
    parking = False
total = (adult_total * 20) + (child_total * 10) + (senior_total * 11) + (wrist_total * 20)
surname = input("What is your surname for the booking? ")
clear()
print("Please pay the cashier")
print("Your total is £" + str(total))
print("I am afraid that you need to pay with cash, in £10 or £20 notes")
notes_10 = int(input("How many £10 notes do you have? "))
notes_20 = int(input("How many £20 notes do you have? "))
def issue_ticket():
    doc = SimpleDocTemplate("receipt.pdf", pagesize=A4)
    elements = []
    data = [
        ["Surname", "Adult", "Child", "Senior", "Wristband", "Parking", "Total"],
        [surname, adult_total, child_total, senior_total, wrist_total, parking, total]
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
    print("Surname: " + surname)
    print("Adult tickets: " + str(adult_total))
    print("Child tickets: " + str(child_total))
    print("Senior tickets: " + str(senior_total))
    print("Wristband tickets: " + str(wrist_total))
    print("Parking pass: " + str(parking))
    print("Total: £" + str(total))
    print("Change: £" + str((notes_10 * 10) + (notes_20 * 20) - total))
    print("Have a nice day!")
    print("Your tickets will be printed now\n")
    issue_ticket()
    print("Your receipt is in 'receipt.pdf'")