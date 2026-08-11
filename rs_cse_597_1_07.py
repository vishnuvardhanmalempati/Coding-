a = int(input('Enter A value:'))
b = int(input('Enter B value:'))
print('Values before swap:',a,b)
a = a ^ b
b = a ^ b
a = a ^ b
print('Values after swapp', a , b)
a , b = b , a
print('Values after swapp', a , b) 
temp = a
a = b
b = temp
print('Values after swapp', a , b)
a = a + b
b = a - b
a = a - b
print('Values after swapp', a , b)
a = a * b
b = a / b
a = a /b
print('Values after swapp', a , b)
