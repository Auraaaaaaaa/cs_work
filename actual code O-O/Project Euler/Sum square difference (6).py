natural_sum = 0
square_of_sum = 0
for  i in range(1,101):
    natural_sum = i**2 + natural_sum 
    square_of_sum = i + square_of_sum 
print((square_of_sum **2)-natural_sum)