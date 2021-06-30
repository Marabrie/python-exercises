import random
Num = int(input("enter number of coin flips:"))

coinflip = 0
h = 0
t = 0

while coinflip < Num:
    coinflip = coinflip + 1
    rand = random.randint(0,1)
    if rand == 1:
        h = h + 1
    else:
        t = t + 1
print ( h,"heads", t,  "tails")