#set num to the value of 2^1000
num = 2**1000
#convert num into a string
strnum = str(num)
#convert num into an array of characters
chararray = list(strnum)
#convert string array into an array of integers
intarray = [int(i) for i in chararray]
#sum and print
print(sum(intarray))