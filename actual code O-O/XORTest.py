def xor(a, b):
    if a == True and b == False:
        return True
    elif a == False and b == True:
        return True
    elif a == True and b == True:
        return False
    elif a == False and b == False:
        return False

print(xor(True, False))
print(xor(False, True))
print(xor(True, True))
print(xor(False, False))
