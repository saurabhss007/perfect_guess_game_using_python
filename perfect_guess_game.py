import random

print("*****Welcome to Perfect Number Guess Game*****")
print("Guess the number chosen by Computer....Maximum attempts 10")
print("Hint : Number exist between 1 to 100 ")

print("Enter 's' to start!!")
# counting number of times user guessed
uGuess = 0

start = input()
# Generating a random numnber
num = random.randint(1,100)
print(num)
if start == 's':
    print("Guess the number...")
    nm = input()
    i = 1
    for i in range(100):
       
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
        uGuess = i + 1
    if int(nm) != num :
        print("YOU LOST Try Again!!!")
else:
    print("Wrong key entered ...Enter 's' to start!!")
print(f"Computer chose : {num}")
print(f"You chose : {nm}")
print(f"Your Score : {uGuess}")

with open ('hscore.txt', 'r') as f :
    if uGuess < int(f.read()) :
        print("NEW HIGH SCORE!!!")
        f.close()
        with open('hscore.txt', 'w') as f:
            f.write(str(uGuess))
            f.close()