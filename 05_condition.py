# condition statement
age = int(input("Enter the age:"))
if(age>=18):
    print("can vote")
else:
    print("cannot vote")


# login program and indentation
# email -> nitish.campusx@gmail.com
# password -> 1234

email = input("Enter your email: ")
password = input("Enter your pass: ")

if email == 'xyz@gmail.com' and password == '1234':
    print('welcome')
elif email == 'xyz@gmail.com' and password != '1234':
    print("incorrect pass")
    password = input("Enter pass again: ")
    if password == '1234':
        print('welcome finally')
    else:
        print('Beta tum se na ho payega')
elif email != 'xyz@gmail.com':
    print('Invalid email')
else:
    print('Not correct')


#find the mininum of 3 given numbers
a =int(input("enter first number: "))
b =int(input("Enter second number: "))
c =int(input("Enter thiird number: "))

if a<b and a<c:
    print("Smallest num is a")
elif b<c:
    print('smallest number is b')
else:
    print('smallest number is c')





#traffic light 
tf= input("colour of light: ")
if(tf=="green"):
    print("Go")
elif(tf=="red"):
    print("Stop") 
elif(tf=="yellow"):
    print("Wait")
else:
    print("Light is broken")   




#Menu driven calculator
menu = input("""
Hi! How can i help you?
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for withdrawl
4. Enter 4 for exit
             """)

if menu =='1':
    print('pin change')
elif menu == '2':
    print('balance')
elif menu == '3':
    print('Withdrawl')
else:
    print('Exit')




# Marks scanario
mark=float(input("enter marks: "))
if(mark>=90):
    print("Grade is: 'A'")
elif(90>mark>=80):
    print("Grade is : 'B'")
elif(80>mark>=70):
    print("Grade is: 'c'")
else:
    print("grade is: 'd'")

marks =[234,34,23,23,423,43]
print(marks)


#Modules in python
# math
import math
math.sqrt(196)

# keyword
import keyword
print(keyword.kwlist)

# random
import random
print(random.randint(1,100))

# datetime
import datetime
print(datetime.datetime.now())

help('modules')