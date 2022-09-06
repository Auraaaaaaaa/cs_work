from random import randint



print("enter your word")



s = input()
a = randint(1, 99099)
new_word = ""
for letter in s:
    new_word = new_word + (chr(ord(letter) + a))
print(new_word)