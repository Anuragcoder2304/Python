name= input("enter your name: ")
print( "welcome ", name)

val = input("Enter some values: ")
print(type(val),val)

name= input("enter name: ")
age= int(input("enter age:"))
marks= float(input("enter marks:"))

print ("wlecom",name)
print("age=",age)
print("marks=",marks)

a= int(input("enter your first number:"))
b= int(input("Enter your second number: "))
print("sum =",a+b)

a= float(input("side of area: "))
area= a*a
print("Area of square: ",area)

a= float(input("Enter first number:"))
b= float(input("Enter second number: "))
average = (a+b)/2
print("Average=",average)

a=int(input("enter number"))
b=int(input("enter number"))
print(a>=b)

str1= "This is a string. \nWe are creating in python"
print(str1) 

a=input("enter name: ")
print(a)
print("length of name",len(a))

string= "Hi #4 i am#igi #kfjg #idjf "
print(string.count("#"))


#Type Conversion
print(5+5.6)
print(type(5),type(5.6))

# Explicit
# str -> int
#int(4+5j)

# int to str
str(5)

# float
float(4)


#Literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

#Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)


# binary
x = 3.14j
print(x.imag)

string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline 
string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)