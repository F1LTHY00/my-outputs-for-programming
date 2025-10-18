import random

print("++++++++++++++++++++")
print("Guessing game...")
print("++++++++++++++++++++")

random_value = random.randint(1,10)
tries = 0
Continue = True

while Continue == True:
    n = eval(input("Guess a random number from 1 to 10:  "))

    tries += 1
    if n == random_value:
        print ("WinneR! , Congratulations!")
        print (f"random value is {random_value}")
        break
    else:
        print ("IncorrecT! , Try again!")
        continue
print (f"You guessed {tries} times")