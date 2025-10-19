#Question no 1
for i in range(1, 11):
    print(i)




#Question no 2
i = 20
while i >= 1:
    print(i)
    i -= 1










#Question no 3
for i in range(2, 11, 2):
    print(i)





#Question no 4
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)








#Question no 5
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)



#Question no 6
for i in range(5):
    print("Happy Birthday!")




#Question no 7
n = int(input("Enter a number: "))
print("The first", n, "terms of the series are:")
for i in range(1, n + 1):
    print(i * i, end=" ")






#Question no 8
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")






#Question no 9
a = 3  # first term
d = 4  # common difference

for i in range(8):
    term = a + i * d
    print(term, end=" ")




#Question no 10
a = 2  # first term
r = 3  # common ratio

for i in range(6):
    term = a * (r ** i)
    print(term, end=" ")



#Question no 11
n = int(input("Enter a positive integer: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of numbers from 1 to", n, "is:", total)





#Question no 12
N = int(input("Enter a positive integer: "))
sum_reciprocal = 0

for i in range(1, N + 1):
    sum_reciprocal += 1 / i

print("The sum of reciprocals from 1 to", N, "is:", round(sum_reciprocal, 2))



#Question no 13
total = 0

for i in range(5):
    num = int(input("Enter a number: "))
    total += num

print("The final running total is:", total)



#Question no 14
n = int(input("Enter a positive integer: "))

if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("The factorial of", n, "is:", fact)




#Question no 15
base = float(input("Enter base number: "))
exp = int(input("Enter exponent: "))

result = 1

if exp > 0:
    for i in range(exp):
        result *= base
elif exp < 0:
    for i in range(-exp):
        result *= base
    result = 1 / result
# if exp == 0, result remains 1

print("Result:", result)




