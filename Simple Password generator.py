print("Enter the number for the characters of the password.")
passlength = int(input())
print(f"Password's length will be {passlength}")

lowercaseletters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z")
uppercaseletters = ("A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
symbols = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "'", ";", ",", ".", ":", "/", "?", "<", ">", "`", "~", "_", "-", "=", "+")
possibilty = lowercaseletters + uppercaseletters + numbers + symbols 
passwordas = possibilty 

import random
passwordad = random.choices(possibilty, k=passlength)
password = "".join(passwordad)
print(password)
