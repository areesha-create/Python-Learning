person = {
    "Student name" : "Areesha Yaqoob"
    "Age" "21"
    "University" "Harvard University"
    "Department" "Department of History of Art and Architecture" 
    "Degree" "Bachelor's in Architecture"
}
 
person["Duration"] = "4 years" 
print("Student information =", person) 
 
isStudent = True
is18 = False
if isStudent:
    print("You are a student.")
else: 
    print("Your are not a student.")
if is18:
    print("You are 18 years old.")
else: 
    print("You are not 18 years old rather, 21 years old.")

Career = ["Landscape Architecture", "Architecture Technology", "Residential Architecture"]
Career.append("Architectural Engineering") 
print("Career:", Career)
 

firstoption = { 
    "Master's  in Landscape Architecture" : "From Harvard University, Delft University of Technology, University of Toronto and University of Manitoba"
}
secondoption = { 
    "Master's in Architecture Technology" : "From Bradford University"
}
thirdoption = { 
    "Master's in Sustainable Architecture" : "From University of Oklahoma, Northeastern University, and RMIT University"
} 
forthoption = { 
    "Master's in Architectural Engineering" : "From Illinois Institute of Technology, University, Milwaukee School of Engineering,  University of Texas at Austin, Aarhus University and Politecnico di Milano internationally"
}
print("First option for Master's degree =", firstoption)
print("Second Option for Master's degree =", secondoption)
print("Third option for Master's degree =", thirdoption)
print("Forth option for a Master's degree =", forthoption) 

print("How many years will it take me to finish my Bachelor's and Master's?") 
print("Bachelor's takes 4 years.")
print("Master's takes 2 years.")
a= 4
b= 2
sum = a+b
print("Total years would be", sum)