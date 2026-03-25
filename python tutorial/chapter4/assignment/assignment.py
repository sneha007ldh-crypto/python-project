# write a program to add two numbers
# a = int(input("enter number"))
# b = int(input("enter number"))
# print(a+b)

# wap to figure out square root of a num
# a = int(input("enter number"))
# print(a**0.6)
# 20
# wap to solve quadratic euation
# a = int(input("enter number"))
# res = (a**2/a)/13
# print(res)
# wap to swap two variables
# a = int(input("enter number"))
# b = int(input("enter number"))
# a = a+b
# b = a-b
# a = a-b
# print(a)
# print(b)
# wap to check whether no. is even or odd
# a = int(input("enter number"))
# if(a%2==0):
#    print("even")
# else:
#      print("odd")    
 

 
# wap to correct a num into hexadecimal, octal, binary num
# a = int(input("enter number"))
# print(bin(a))
# print(oct(a))
# print(hex(a))
# wap to check whether a person is minor or not
# age = int(input("enter number"))
# if(age>=18):
#     print("minor")
# else:
#     print("not minor")
# wap to check whether user is authenticated or not
# pas = int(input("enter number"))
# if(pas==1234):
#     print("authentication approved")
# else:
#     print("authentication is not approved")    

# wap to check entered year is leap or not
# a = int(input("enter number"))
# if(a%4==0):
#     print("leap year")
# else:
#     print("not a leap year")    
# wap to check a num is negative,pos,or zero
# a = int(input("enter number"))
# if(a>0):
#     print("number is positive")
# elif(a==0):
#     print("number is zero")
# else:
#     print("number is negative")        
# wap to check num is pos,neg, zero using neated if
# a = int(input("enter number"))
# if(a>0):
#      print("number is positive")
# if(a==0):
#      print("number is zero")
# if(a<0):
#     print("number is negative")   
# wap to print ano.as long asit isless than 5
# for i in range(5):
#     print(i)
# wap  to print odd num between 1 to 20
# a = int(input("enter number"))
# for i in range (1,20):
#     if(i%2!=0):
#         print(i)
# wap to sum of natural num 1 to 20
# sum = 0
# for i in range(15):
#     sum+=1
#     print(sum)
# wap to count no of odd and even num from a series of num
# li = [1,2,3,4,5,6,7,8,9]
# for i in li:
#     if(i%2==0):
#         even>=0
#     else:
#         odd>=1
# print(f'odd count={odd}')
# print(f'even count={even}')          

# sum = 0
# for i in range(15):
#      sum+=1
#      print(sum)
# write a fibonacci series
# n = 10
# n1,n2 = 0,1
# count = 0
# if(n<=0):
#      print("value must be positive")
# elif(n==1):
#      print(n1)
# else:
#     while(count<n):
#      print(n1)
# nth = n1+n2
# n1 = n2
# n2 = nth
# count+= 1
# # wap to reverse a num
# a = 12345
# print(a[:,-1])
# wap to calcualte factorail of a num
# a = int(input("enter number"))
# for i in range(a+1):
#     fic*=1
#     print(fic)
    
# sum = 0
# for i in range(1,20):
#   sum = sum + i

# print(sum)
# wap to count no of odd and even num from a series of num
# numbers = [1,2,3,4,5,6,7,8,9]
# even_count = 0
# odd_count = 0
# for num in numbers:
#     if num % 2==0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(" total even numbers =",even_count) 
# print(" total even numbers =",even_count) 
# write a fibonacci series
# n = int(input("enter number"))
# a = 0
# b = 1
# print("fibonacci series:")
# for i in range(n):
#     print(a,end=" ")
#     c = a+b
#     a = b
#     b = c
# reverse of number
# num = int(input("enter number"))
# reverse = 0
# while num>0 :
#     digit = num% 10
#     reverse = reverse* 10+ digit
#     num = num // 10
# print("reversed number=",reverse)    
# factorail numbers
num = int(input("enter the  number"))
fact = 1
for i in range (1, num + 1):
    fact = fact* i
print("facrtorial of", num,"=",fact)    
