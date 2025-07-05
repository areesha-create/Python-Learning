print("Pick a length unit to convert into:")
print("1. cm")
print("2. m") 
choice = input("To select type 1 or 2.")

useramount = int(input("Type the value:"))

if choice == "1":
    result = useramount / 100
    print(f"{useramount} centimeters is {result} meters.")
elif choice == "2":
    result2 = useramount * 100
    print(f"{useramount} meters is {result2} centimeters.")
else:
    print("Type 1 or 2")