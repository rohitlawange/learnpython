line = '-------------------\n'

#basic output
print("hello world")
print(line)

#conditions
if(5>2):
    print('5 is greater than 2')
if(2<5):
    print('2 is less than 5')
print(line)

#variables
x=5
print(x,'+',x,'=',x+x)
y='ha'
print(y)
print(y*x)
print(line)

#multi line comment
"""
this is a multiline comment
here I can write multiple lines as comment
"""

#casting
x = str(3) #string
y = int(3) #int
z = float(3) #float

print(type(x))
print(type(y))
print(type(z))
print(line)

#quotes
x = "John"
print(x)
#is same as
x = 'John'
print(x)
print(line)

#variable names can start with an underscore
print(1,2,3,4,sep='+')
print('=','10')
_name = 'rohit'
print(_name,'\n',line, sep='')#use of sep


#multiple variables
x,y,z = 'x','y','z'
print(x,y,z)
x=y=z='xyz'
print(x,y,z)
print(line)

#collection
fruits = ["banana","apple","mosambi"]
print(fruits)

#unpacking the collections, I didnt know of this
x,y,z = fruits
print(x,y,'and',z)
print(line)

#string concatenation
print("I","am","awesome")
print("I"+"am"+"awesome")
print(line)

#number addition
x=5
y=5
print(x+y)
z=5.5
print(x+z)
print(line)

#string concatenation of a number and str is not possible using +
#print(5+"rohit") #this line wont work

print(str(5)+"rohit")

#scope
m = "even"
if(3>2):
    print(m)
    m = "odd"
    print(m)

print(m)
print(line)
mm="even"
print(mm)
def myfunc():
    mm = "odd"
    print(mm)

myfunc()
print(mm)
print(line)

#GLOBAL SCOPE
def myfunc():
    global xx
    xx = "global"
    print(xx)

myfunc()
print(xx)