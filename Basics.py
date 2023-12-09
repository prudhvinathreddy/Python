#printing strings
print("Hello")

#arithmatic operations
print(2+2)

print(5-2)

print("Two"+"2")

print(2*5)
print(2**3)
print(100/3)
print(100//3)

a=20;b=30;
print(a+b,a-b)
print(a*2*b)

#type of a variable
#casting
a=100
print(type(a))
a="100"
print(type(a))
#assign the type of variable
a=str(200)
print(type(a))
a=float(34)
print(type(a))

#assigning multiple variables
a,b,c="apple","bat","cat"
print(a,b,c)

#assigning same values to variables
a=b=c="orange"
print(a,b,c)

#LISTS
Games=['cricket','football','kabaddi']
a,b,c = Games
print(a,b,c)

#how to use PRINT function
print(a+b+c)

#global Variables
x='awesome' #global variable can be used inside a fun or outside
def fun():
    print("Python is "+ x)
fun()

def fun2():
    x="fantastic" #Local variable used inside function
    print("Python is "+x)

fun2()
print("Python is "+x)


#Random numbers

import random
print(random.randrange(1,10))

#strings
a="""hgsdhf jhbsjad jhbdj
sdfhkjhkn kjkldnllb jhgytasfd"""
print(a)
#strings are arrays
a='Hello World'
print(a[6])
print(len(a))

#loop string
for x in a:
    print(x)

for x in "hello":
    print(x)


for x in range(0,10):
    print(x*2)

#check string presence
txt="Hello world i am python"
print("python" in txt)
print("pys" in txt)
if "pys" in txt:
    print("yes, we found it")
else:
    print("we are sorry")

#slicing strings
x="Hello, Python "
print(x[:5]) #from start
print(x[2:7]) #in between
print(x[2:]) #from end
print(x[-9:])#negative slicing

#modifying strings
print(x.upper()) #upper case
print(x.lower()) #lower case
print(x.strip()) #remove white spaces at begining or end
x="Hello, Python"
#replace string
print(x.replace("H","P"))
#split string
print(x.split(" "))
