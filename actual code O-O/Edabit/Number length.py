def num_length(num):
    length = 0
    for i in str(num):
        length += 1
    return length
print(num_length(input()))