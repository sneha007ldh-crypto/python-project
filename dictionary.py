# dictionary is a data strucure in  which we store data in key values pairs.it is ordered and changable and do not allow duplicates.
student = {
    "name" : "sneha",
    "class" : "bca",
    "age"  :20,
}
print(student)

# create dictionary  in other way
my_dict ={"name":"sneha","age": 20,"course":"bca"}
print(my_dict)

# empty dictionary
empty_dic ={}
print(empty_dic)

# other method .using dict constructor
person = dict(name ="sneha",age =20,course ="bca")
print(person)
# method 3  using list of tuples
student  = dict([("name","sneha"),("age",20)])
print(student)

# acess dictionary values
student = {
    "name" : "sneha",
    "class" : "bca",
    "age"  :20,
}
print(student)
print(type(student)) # we check atype of dictionary
print(student["name"]) # we can access a single single value by using this method
print(student["age"])
# dicetionary methods built in methods
# values  return  a list of all values from dictionary
print(student.keys())# it ret only keys from dict
print(student.values()) # it ret values from dict
print(student.items()) # it ret both key with value
print(student.get("name")) # in which we get value acc to our need in case if value is not present in it then it not give any error
# nested dictionary it contain other dictionary which is useful for complex data
employee1 ={
    "name" : "sneha",
    "class" : "bca",
    "age"  :20,
}

employee2 ={
    "name" : "krishna",
    "class" : "bca",
    "age"  :21,
}
print(employee1)
print(employee2["name"])

# update to update value
student.update({"age": 21, "class": "bba"})
print(student)
#pop to remove specify key
student.pop("age")
print(student)
# pop item to remove last value 
student.popitem()
print(student)
# clear to delete all data
student.clear()
print(student)
# copy is used to make a same copy of a dictionary copy ma new data change kar sakta hai but original same rehta hai
student = {"name": "sneha"}
new_student = student.copy()
new_student["age"] = 25
print(new_student)
# setdefault new key ko add karta hai
student = {"name": "sneha"}
student.setdefault("year", 2026)
print(student)
# fromkeys ek jaisa structure bananaek hi value initalize karke sab ma likh dena
keys = ["name", "age", "class"]
student = dict.fromkeys(keys, "unknown")
print(student)
# len we check how many keys are there
print(len(student))
# add, modify and remove items
# add to new key with value paired
student['email']="sneha007lad@gamil.com"
print(student)
# modify
student['email']="sneha007ldh@gamil.com"
print(student)
# remove we use delete or pop
del student["age"]
print(student)
# pop
email = student.pop("email")
print(email)
print(student)
# iteration used for loops through keys
for keys in student.keys():
    print(keys) # we access only keys

for keys,value in student.items():
    print(keys,value) # we access both

for value in student.values(): # we access value of keys
    print(value)
# we print with condition ke sath
marks = {"math": 80, "eng": 95, "sci": 70}

for key, value in marks.items():
    if value > 80:
        print(key, value)
# count karna loop + counter
student = {"name": "sneha", "age": 20, "class": "bca"}

count = 0

for key in student:
    count += 1

print("Total keys:", count)
# convert dic into uppercase
student = {"name": "sneha", "class": "bca"}

for key, value in student.items():
    print(key.upper(), value.upper())
# we sum all the values
marks = {"math": 80, "eng": 90, "sci": 70}

total = 0

for value in marks.values():
    total += value

print("Total:", total)    
# dictionary comprehnsions
# syntax  new_dict ={{key: value for item in iterable}
new_dict ={1,2,3,4,5}
square ={x:x**2 for x in new_dict}
print(square)
# second one example  even numbers
new_dict ={1,2,3,4,5}
square ={x:x**2 for x in new_dict if x%2==0}
print(square)
# for odd number
new_num ={1,2,3,4,5,6}
odd_num ={x:x**2 for x in new_num if x%2==1}
print(odd_num)
# for string  example
st= {"apple","banana","cherry"}
len_dict ={word:len(word) for word in st}
print(len_dict)
# dictionary in other dictionary
marks ={"eng":50,"maths":78,"sci":67}
new_marks ={k:v+5 for k,v in  marks.items()}
print(new_marks)