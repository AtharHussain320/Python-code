
#Question 1:
#Print Your Name with your Father name and Date of birth using suitable escape sequence character.

print("Name:\tAthar Hussain\nFather's Name:\tMr. Hussain\nDate of Birth:\t01-01-2000")



#Question 2
#Write your small bio using variables and print it using print function.

name = "Athar Hussain"
age = 24
course = "Cloud Data Engineering"
institute = "SMIT (Saylani Mass IT Training Center)"

print("My name is", name)
print("I am", age, "years old.")
print("I am studying", course, "at", institute)


#Question 3:
#Write a program in which use all the operators we can use in Python.

a = 10
b = 3

# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Comparison Operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater:", a > b)
print("Less:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)

# Logical Operators
print("Logical AND:", a > 5 and b < 5)
print("Logical OR:", a > 5 or b > 5)
print("Logical NOT:", not(a > b))

# Assignment Operators
x = 5
x += 2
print("Assignment +=:", x)

# Bitwise Operators
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)





# Question 4:

#Completes the following steps of small task:

#Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables

#Mention Variable of Total Marks and assign 300 to it

#Calculate Percentage


english = 85
islamiat = 90
maths = 80
total_marks = 300

obtained = english + islamiat + maths
percentage = (obtained / total_marks) * 100

print("Obtained Marks:", obtained)
print("Percentage:", percentage, "%")




# Part - 2 Python Basics (Conditional Statements)
#Question 1:

#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.


salary = int(input("Enter your salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 0.05
    print("Your bonus is:", bonus)
else:
    print("No bonus")




# Question 2:

#Write a program to check whether a person is eligible for voting or not.


age = int(input("Enter your age: "))

if age > 17:
    print("Eligible for voting")
else:
    print("Not eligible for voting")



# Question 3:

#Write a program to check whether a number entered by user is even or odd.


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")




# Question 4:

#Write a program to check whether a number is divisible by 7 or not.

num = int(input("Enter a number: "))

if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")



#Question 5:

#Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".

num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Hello")
else:
    print("Bye")




#Question 6:

#Electricity Bill Calculation.


units = int(input("Enter number of units: "))

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + ((units - 300) * 10)

print("Total Bill: Rs.", bill)


# Question 7:

#Write a program to display the last digit of a number



num = int(input("Enter a number: "))
print("Last digit is:", num % 10)




#Question 9:

#Take values of length and breadth of a rectangle from user and print if it is square or rectangle.


length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

if length == breadth:
    print("It is a Square")
else:
    print("It is a Rectangle")




# Question 10:

#Take two int values from user and print greatest among them.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greatest is:", a)
else:
    print("Greatest is:", b)




#Question 11:

#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Suppose, one unit will cost 100.



qty = int(input("Enter quantity: "))
cost = qty * 100

if cost > 1000:
    cost = cost - (cost * 0.10)

print("Total Cost:", cost)




# Question 12:

#Grading system:


marks = int(input("Enter marks: "))

if marks < 25:
    print("Grade: F")
elif marks < 45:
    print("Grade: E")
elif marks < 50:
    print("Grade: D")
elif marks < 60:
    print("Grade: C")
elif marks < 80:
    print("Grade: B")
else:
    print("Grade: A")



#Question 13:

#Take input of age of 3 people by user and determine oldest and youngest among them.


a = int(input("Enter age of person 1: "))
b = int(input("Enter age of person 2: "))
c = int(input("Enter age of person 3: "))

print("Oldest age is:", max(a, b, c))
print("Youngest age is:", min(a, b, c))




#Question 14:

#Attendance check.

classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

percentage = (classes_attended / classes_held) * 100
print("Attendance Percentage:", percentage)

if percentage >= 75:
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam")




# Question 15:

#Attendance check with medical cause.


classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))
medical = input("Do you have medical cause? (Y/N): ")

percentage = (classes_attended / classes_held) * 100
print("Attendance Percentage:", percentage)

if percentage >= 75 or medical.upper() == 'Y':
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam")


#Question 16:
#Check leap year.

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")



# Question 17:

#Service rules based on age, gender, and marital status.


age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")

if gender.upper() == "F":
    print("She will work only in urban areas.")
elif gender.upper() == "M":
    if 20 <= age <= 40:
        print("He may work anywhere.")
    elif 40 < age <= 60:
        print("He will work only in urban areas.")
    else:
        print("ERROR")
else:
    print("Invalid input")
