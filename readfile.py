import random
r = random.randint(0,13)
f = open("list.txt","r")
##print(f.read())
line = f.readlines()
print(line[r])