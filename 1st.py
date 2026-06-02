import random
r = random.randint(1,100)
num_list = []
count = 1
a = int(input("enter your number to guess!"))
num_list.append(a)
while a != r:
    if a<r:
        print("your guess is lower than actual number🙂")
    elif a>r:
        print("your guess is higher than actual number😊")
    a = int(input("enter your number to guess!"))
    num_list.append(a)
    count = count + 1
if a==r:
    print("perfect guess😍")
    print("the number you have guessed!")
    for l in num_list:
        print(l)
    print(f"you have made {count} guesses")

