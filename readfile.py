import random
r = random.randint(0,13)
s = random.randint(1,26)
f = open("list.txt","r")
##print(f.read())
line = f.readlines()
text = line[r]

def shift(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 +97)
    return result

print(shift(text,s))