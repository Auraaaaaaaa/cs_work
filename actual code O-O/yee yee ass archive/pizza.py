total_cost = 0.00

print("Thick or thin?")
bread_type = input()
print("8 inch, 12 inch or 14 inch?")
size = input()
print("Mahgarita, Vegetable, Vegan, Hawaiian or Meat Feast")
topping = input()
print("Do you have a voucher code? Enter it here, or say NONE")
voucher = input()
if bread_type != "thin":
  total_cost = 10.00
else:
  total_cost = 8.00
if topping == "Mahgarita":
  total_cost = total_cost
elif topping == "Vegetable" or "Vegan":
  total_cost = total_cost + 1
elif topping == "Hawaiian" or "Meat Feast":
  total_cost = total_cost + 2
if voucher == "FunFriday":
  total_cost = total_cost - 1


print(f"Your total cost is: £{total_cost}")

