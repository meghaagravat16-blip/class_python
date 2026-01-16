# 1. Calculate Simple Interest
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)


# 2. Find maximum of 2 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Maximum number is:", max(a, b))


# 3. Print numbers 1 to 5
for i in range(1, 6):
    print(i)


# 4. Find length of a string
s = input("Enter a string: ")
print("Length of string:", len(s))


# 5. Print a welcome message
print("Welcome to Python Programming!")


# 6. Print first character of a string
s = input("Enter a string: ")
print("First character:", s[0])


# 7. Print last character of a string
s = input("Enter a string: ")
print("Last character:", s[-1])


# 8. Check positive or negative number
n = int(input("Enter a number: "))
if n >= 0:
    print("Positive number")
else:
    print("Negative number")


# 9. Add 3 numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
print("Sum =", x + y + z)


# 10. Take an input from user
name = input("Enter your name: ")
print("Hello,", name)