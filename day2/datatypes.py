line = "--------------"
def ln():
    print(line)

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

#complex dataclasses

x = 10j
print(x)

x= ["apple","banana","orange"]
print(x)

x = ("apple","banana","mosambi")
print(x)

#what is the difference between list and a tuple
# can we unpack a tuple
a,b,c = x

print(a)
print(b)
print(c)

x= range(3)

print(x)

a,b,c = x

print(a)
print(b)
print(c)

ln()

#dict
x = {"name" : "rohit", "age":26}
print(x)



ln()

x = {"apple","apple","apple","banana"}
print(x)
ln()


# set x = {"apple","apple","apple","banana"}
# list x = ["apple","apple","apple","banana"]
# tupple x = ("apple","apple","apple","banana")


x = True
print(x)

#bytes
x = b"Hello"
print(x)

#bytearray
x = bytearray(5)
print(x)

#memoryaddress
x = memoryview(bytes(5))
print(x)

#NoneType
x = None
print(x)

#random
import random

print(random.randrange(1,10))


