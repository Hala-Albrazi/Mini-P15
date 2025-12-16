import random
import string
print("Welcome to the password generator!")
length = int(input("Enter the number of the characters in the password: "))
letter = int(input("Enter the number of letters in the password: "))
number = int(input("Enter the number of numbers in the password: "))
symbol = int(input("Enter the number of sybmols in the password: "))
all = (letter + number + symbol)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if length != all:
    print("Invalid input!!!")
else:
    p1 = random.choices(string.digits, k=number)
    p2 = random.choices(string.ascii_letters, k=letter)
    p3 = random.choices(string.punctuation, k=symbol)
    password = p1 + p2 + p3
    random.shuffle(password)
    final = "".join(password)
    print(f"Generated password: {final}")
