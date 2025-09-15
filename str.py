#Q1. Write a program that accepts a string from user. Your program should
# count and display number of vowels in that string



text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)




#Q2. Write a program that reads a string from keyboard and display:

#The number of uppercase letters in the string

#The number of lowercase letters in the string

#The number of digits in the string

#The number of whitespace characters in the string




text = input("Enter a string: ")
upper = lower = digit = space = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
    elif char.isspace():
        space += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Spaces:", space)





#Q3. Write a Python program that accepts a string from user. Your program should
# create and display a new string where the first and last characters have been exchanged.
# Example: if user enters "HELLO", new string would be "OELLH"




text = input("Enter a string: ")

if len(text) > 1:
    new_text = text[-1] + text[1:-1] + text[0]
else:
    new_text = text  

print("New string:", new_text)





#Q4. Write a Python program that accepts a string from user.
# Your program should create a new string in reverse of first string and display it.
# Example: if user enters "EXAM", new string would be "MAXE"



text = input("Enter a string: ")
new_text = text[::-1]
print("Reversed string:", new_text)








#Q5. Write a Python program that accepts a string from user. 
#Your program should create a new string by shifting one position to left.
# Example: if user enters "examination 2021", new string would be "xamination 2021e"




text = input("Enter a string: ")

if len(text) > 1:
    new_text = text[1:] + text[0]
else:
    new_text = text

print("New string:", new_text)







#Q6. Write a program that asks the user to input his name and print its
# initials. Assuming that the user always types first name, middle name and last name and does not include any unnecessary spaces.
# Example: if user enters "Ajay Kumar Garg", the program should display "A. K. G."
#(Do not use split() method)




name = input("Enter your full name: ")

words = name.split()
initials = ""

for word in words:
    initials += word[0].upper() + ". "

print("Initials:", initials.strip())




#Q7. A palindrome is a string that reads the same backward as forward. For example, "dad", "madam", and "radar".
# Write a program that determines whether the string is a palindrome.
#(Do not use reverse() method)




text = input("Enter a string: ")
is_palindrome = True

for i in range(len(text)):
    if text[i] != text[-(i+1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")








#Q8. Write a program that display following output from "SHIFT":



text = "SHIFT"

for i in range(len(text)):
    rotated = text[i:] + text[:i]
    print(rotated)





#Q9. Write a program in Python that accepts a string to setup a password.
# Your entered password must meet the following requirements:

#The password mist be at least 8 characters long.

#It must contain at least one uppercase letter

#It must contain at least one lowercase letter

#It must contain at least one numeric digit

#Your program should perform this validation.



password = input("Enter a password: ")

# Conditions
has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(not ch.isalnum() for ch in password)
long_enough = len(password) >= 8

if has_upper and has_lower and has_digit and has_special and long_enough:
    print("Password is valid ✅")
else:
    print("Password is invalid ❌")
    print("Requirements:")
    print("- At least 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character")
