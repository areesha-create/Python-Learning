
import random
number = random.randint(1,10)
guess = int(input("Enter the number!"))
while guess != number:
    print("Wrong number! Try again.")
    guess = int(input("Enter the number again!"))
print("Correct number! Congratulations!")