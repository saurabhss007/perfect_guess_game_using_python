import random

print("*****Welcome to Perfect Number Guess Game*****")
print("Guess the number chosen by Computer....Maximum attempts 10")
print("Hint : Number exist between 1 to 100 ")

print("Enter 's' to start!!")

i = 0
start = input()
# Generating a random numnber
num = random.randint(1,100)
if start == 's':
    print("Guess the number...")
    nm = input()
    for i in range(10):
       
        if int(nm) == num :
            print("Correct Guess!! You are a genius!")
        elif int(nm) < num :
            print("Guess a larger number...")
            nm = input()
            if int(nm) == num :
                 print("Correct Guess!! You are a genius!")
                 break
        elif int(nm) > num :
            print("Guess a lower number...")
            nm = input()
            if int(nm) == num :
                 print("Correct Guess!! You are a genius!")
                 break
        i = i + 1
    if int(nm) != num :
        print("YOU LOST Try Again!!!")
else:
    print("Wrong key entered ...Enter 's' to start!!")
print(f"Computer chose : {num}")
print(f"You chose : {nm}")