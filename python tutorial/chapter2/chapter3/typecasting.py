# casting in python to change the datatypes 
# a = 1
# print(type(a)) 
# b ="1"
# print(type(b))
# print(a+b)  # it through error bez int and string cant be added

# way to typcast 
a = 1
print(type(a)) 
b ="1"
print(type(b))
c = int(b)
print(a+int(b))  # first way
print(a+c)      # second way  we write to print the variable
  
  # we cant convert the string into  int
# name =  " sneha"
# newname = int(name)

# we convert int to string
mynum = 26
newnum = str(mynum)  # first we convert into string
print(type(newnum))  # now int change into string bez we change
print(newnum)  # now number can be a string value 
# float to int
f1 = 22.7
print(type(int(f1)))
# second way to write
f1 = 22.3
f2 = int(f1)
print(type(f2))
print(f2)
# int to float
in1 = 24
in2 = float(in1)
print(type(in2))
print(in2)

# implicit casting
var1 = 10
var2 =  23.3
v3 = var1+var2
print(var1+var2)
print(type(v3))

# explicit casting
# convert string into integer
str_num = "26"
int_num = int(str_num)
print(int_num)
print(type(int_num))
# convert a value to boolean
bool(0)
print(bool(0))

bool(1)
print(bool(1))
# another way to write a code
a = bool(0)
print(a)
print(type(a))

#  write a code to write both datatype and boolean value like (T/F)

a0 = bool(0)
print(a0)
print(type(a0))

a1 = bool(1)
print(a1)
print(type(a1))





