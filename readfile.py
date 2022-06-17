import random
import re

r = random.randint(0,12)
s = random.randint(1,25)
f = open("list.txt","r")
##print(f.read())
print(r)
print(s)
line = f.readlines()
text = line[r]

def shift(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (re.findall("[a-zA-Z]", char)):
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            else:
                result += chr((ord(char) + s-97) % 26 +97)
        else:
            result += char
    return result

cipher = shift(text,s)
print(cipher)

ff = open("README.md","r")
fline = ff.readlines()
fline[2] = cipher

with open("README.md","w", encoding="utf-8") as file:
   file.writelines(fline) 

print(fline)