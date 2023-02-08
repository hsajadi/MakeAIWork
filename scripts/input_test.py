#!/usr/bin/env python

num1 = eval ( input( "Enter the first number: ") ) 

num2 = eval( input ( "Enter the second number: " ) )
num3 = eval( input ( "Enter the third number: " ) )
num4 = eval ( input ("Enter the fourth number: ") )
print("(number1 - number2)/(number3 + number4)", (num1-num2)/(num3+num4))


num5 = eval(input("Enter a number: "))
print("Your number squared:", num5*num5)



from random import randint
q = randint(1,50)
y = randint(2,5)
print(q**y)


num6 = eval ( input( "Enter a number of seconds: ") )
z = num6//60
a = num6%60
print(num6, "is", z, "mitutes and", a, "seconds")


x = str(input("please enter a string: "))

print(len(x))

print(x*10)

print(x[0])

print(x[0:3])

print(x[-3:])

print(x[::-1])

