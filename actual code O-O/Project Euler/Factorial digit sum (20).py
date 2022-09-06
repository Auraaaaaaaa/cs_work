def factorialise(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return(factorial)
combinednums = factorialise(100)
#put all digits of combinednums into an array
numsarray = []
for i in str(combinednums):
    numsarray.append(int(i))
#change the string array into an int array
numsarray = [int(i) for i in str(combinednums)]
print(sum(numsarray))