print("I need to do some simple calculations." \
"The first one is:" \
" Find the total amount of candies Ayeza has in her both hands.")
leftHand = 12
rightHand = 5 
print("In the Left Hand she has: 12 candies")
print("In the right hand she has : 5 candies")
print("Total candies: ?")
result = leftHand + rightHand
print("Total candies:", result)

print("The second calculation is: Find how many years old is Ayeza?")
birthYear = 1998
currentYear = 2025 
print("She was born in 1998.")
print("The current year is 2025.")
print("Age: ?")
result = currentYear - birthYear
print("Age:", result)

print("The third calculation is: Ayeza wants to buy 3 boxes which contain 113 small toys per box. How many wil she have in total?")
toysperBox = 113
amountofBoxes = 3
print("Their are 113 small toys in 1 box.")
print("Their are 3 boxes.")
print("Total toys: ?")
result = toysperBox * amountofBoxes
print("Total toys:", result) 

print("The forth calculation is: Ayeza has 14 pencils. She wants to share with her 7 friends. How many pencils will everyone have?" )
pencilsAmount = 14
freindsAmount = 7
print("Amount of Pencils: 14")
print("Amount of friends: 7")
result = pencilsAmount / freindsAmount
print("Pencils per person:?")
print("Pencils per person:", result)

print("The fifth calculation is: Ayeza needs to find the answer on the question on her math test. The question is what is 15 divided by 2? Find the answer to help Ayeza.")
print("15 divided by 2 will be: ?")
xY = 15
yZ = 2
result = xY // yZ 
print("15 divided by 2 will be:", result)

print("The sixth calcultaion is: A teacher has 50 small gift bags to give out. She wants to give each student 3 gift bags. If there are 18 students in the class, how many gift bags will be left over after everyone receives their share?") 
gifts = 50
students = 18
result = gifts % students
print("Number of gifts left: ?")
print("Number of gifts left:", result)

print("The seventh calculation is: Ayeza have a special type of plant in her garden that doubles its number of leaves every week. If it starts with just 2 leaves, how many leaves will it have after 5 weeks?")
leaves = 2
weeks = 5
result = leaves ** weeks
print("The number of leaves now: ?")
print("The number of leaves now:", result)
