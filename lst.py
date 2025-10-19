#Question no 1
# Program to print alternate elements of a list

lst = []
n = int(input("Enter number of elements: "))

for i in range(n):
    val = input(f"Enter element {i+1}: ")
    lst.append(val)

print("Alternate elements of the list are:")
for i in range(0, len(lst), 2):
    print(lst[i])








#Question no 2
# Program to reverse list without using reverse()

lst = []
n = int(input("Enter number of elements: "))

for i in range(n):
    val = input(f"Enter element {i+1}: ")
    lst.append(val)

reversed_list = []
for i in range(len(lst) - 1, -1, -1):
    reversed_list.append(lst[i])

print("Reversed list:", reversed_list)







#Question no 3
# Program to find largest number in list without max()

lst = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    lst.append(num)

largest = lst[0]
for num in lst:
    if num > largest:
        largest = num

print("Largest number is:", largest)









#Question no 4
# Rotate list elements (shift all one position to the left)

lst = [1, 2, 3, 4, 5]
first = lst[0]

for i in range(len(lst) - 1):
    lst[i] = lst[i + 1]

lst[-1] = first
print("Rotated list:", lst)








#Question no 5
# Program to delete a given word from a string

text = input("Enter a sentence: ")
word = input("Enter the word to delete: ")

words = text.split()
new_sentence = ""

for w in words:
    if w != word:
        new_sentence += w + " "

print("Updated sentence:", new_sentence.strip())









#Question no 6
# Program to convert date format

date = input("Enter date (mm/dd/yyyy): ")
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

mm, dd, yyyy = date.split("/")
month_name = months[int(mm) - 1]

print(f"{month_name} {int(dd)}, {yyyy}")







#Question no 7
# Program to capitalize first letter of each word

sentence = input("Enter a sentence: ")
words = sentence.split()

new_sentence = ""
for word in words:
    new_sentence += word.capitalize() + " "

print("Updated sentence:", new_sentence.strip())







#Question no 8
# Program to find sum of each row of a matrix

matrix = [
    [2, 11, 7, 12],
    [5, 2, 9, 15],
    [8, 3, 10, 42]
]

for i in range(len(matrix)):
    row_sum = 0
    for j in range(len(matrix[i])):
        row_sum += matrix[i][j]
    print(f"Sum of row {i + 1} = {row_sum}")







#Question no 9
# Program to add two matrices

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Sum of matrices:")
for r in result:
    print(r)










#Question no 10
# Program to multiply two matrices

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("Product of matrices:")
for r in result:
    print(r)
