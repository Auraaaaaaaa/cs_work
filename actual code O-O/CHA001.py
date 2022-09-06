pndcoins = 0
twopndcoins = 0
fiftyp = 0
twntyp = 0
tenp = 0
fivep = 0
twop = 0
onep = 0
print("Enter a number of pence to do things to:")
num = int(input())
def e():
    if num - 200 >= 0:
        twopndcoins = twopndcoins + 1
        num = num - 200
        e()
    if num - 100 >= 0:
        pndcoins = pndcoins + 1
        num = num - 100
        e()
    if num - 50 >= 0:
        fiftyp = fiftyp + 1
        num = num - 50
        e()
    if num - 20 >= 0:
        twntyp = twntyp + 1
        num = num - 20
        e()
    if num - 10 >= 0:
        tenp = tenp + 1
        num = num - 10
        e()
    if num - 5 >= 0:
        fivep = fivep + 1
        num = num - 5
        e()
    if num - 2 >= 0:
        twop = twop + 1
        num = num - 10
        e()
    if num - 1 >= 0:
        onep = onep + 1
        num = num - 1
        e()

print(f"£2: {twopndcoins} £1: {pndcoins} 50p: {fiftyp} 20p: {twntyp} 10p: {tenp} 5p: {fivep} 2p: {twop} 1p: {onep}")