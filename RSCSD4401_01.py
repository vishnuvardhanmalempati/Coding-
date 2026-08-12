#one
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("Name:", name)
print("Age:", age)
print("City:", city)

#two
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)


#three
r = float(input("Enter radius: "))

area = 3.14 * r * r

print("Area of circle =", area)


#four
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)

#five
c = float(input("Enter Celsius: "))

f = (c * 9/5) + 32

print("Fahrenheit =", f)

#six
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3

print("Average =", average)

#seven
a = input("Enter first value: ")
b = input("Enter second value: ")

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

#eight
seconds = int(input("Enter seconds: "))

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)


#nine
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    print("Result =", a / b)
else:
    print("Invalid operator")