fib_nums = []
fib_nums.append(1)
fib_nums.append(1)
i = 2
while len(str(fib_nums[i-1])) < 1000:
    fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
    i += 1
print(i)