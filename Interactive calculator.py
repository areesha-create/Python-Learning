# ask the user to enter your value 
first_value = float("Enter 1st value:") # python will prompt: Enter 1st value
print(first_value) # print the value
if first_value: # handle error and ask to type the value again
    first_value = "0"
    print("Error")
    print("Write another value")
 
which_operation = input("Enter the operation.") 
if which_operation:
    which_operation = "+"
    print("added into")
elif which_operation:
    which_operation = "-"
    print("subtracted by")
elif which_operation:
    which_operation = "*"
    print("multiplied by")
elif which_operation:
    which_operation = "/"
    print("divided by")
else:
    #handle the error
# ask the user to enter your second value 
second_value = float("Enter 2nd value:") # python will prompt: Enter 2nd value
print(second_value)

