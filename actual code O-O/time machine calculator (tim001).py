def beans():
    print("hello")
    print("Enter the time in the future, with no colon between the numbers")
    a = int(input())
    if (a > 2359):
        print("No! That is a time in the future you supine protoplasmic invertebrate jelly")
        beans()
    elif (a < 1000):
        print("no thats not 24-hr time silly")
        beans()
    print("Enter a new time to calculate against")
    b = int(input())
    if b > a:
        print("That's in the future from the first time! Try again")
        beans()
    c = a - b
    minutes = c % 100
    hou = c // 100
    if minutes > 59:
        minutes = minutes - 60
        hou = hou + 1
    print(""+str(hou) + " hours and "+str(minutes) + " minutes")
    exit()
beans()