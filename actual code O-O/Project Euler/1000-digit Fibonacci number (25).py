#calculate fibbonaci until the number has 1000 digits, and prrint the index of the number
def get_digits(n):
    return len(str(n))
num = 0
n1, n2 = 0, 1
count = 0
while get_digits(num) <= 1000:
    num = n1 + n2
    n1 = n2
    n2 = num
    count += 1
print(count)