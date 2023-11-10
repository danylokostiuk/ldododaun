import random
number = int(input())
a = random.randint(1,100)
print(a)
atry = 4
while 0 <= atry:
    if number != a:
        atry = atry - 1
        print("nepravilno")
        number = int(input())
    elif number == a:
        print("pravilno")
        break
    else:
        print("error")
