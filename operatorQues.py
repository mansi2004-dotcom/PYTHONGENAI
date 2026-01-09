#Question1.
a=input("enter name of student: ")
b=input("enter class of student: ")
c=input("enter section of class: ")
sub1=int(input("enter marks of science: "))
sub2=int(input("enter marks of maths: "))
sub3=int(input("enter marks of computer: "))
sub4 =int(input("enter marks of social science: "))
sub5=int(input("enter marks of hindi: "))
total_marks=500
total=sub1+sub2+sub3+sub4+sub5
print(total/total_marks*100)
# #  Question2
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c= int(input("enter third number: "))
result =a+b+c
print(result)
# # Question 3
num=int(input("enter a number: "))
print(num**2)
# Question 4
temp=input("enter the temperature in celsius: ")
print(float(temp))
# ## Question 5
import math
celsius = int(input("enter value: "))
farenheit=(celsius*9/5)+32
print(farenheit)
faren=int(input("enter value: "))
cels=(faren*9/5)+32
print(cels)
# ##Question 6
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
result=num1%num2
print("remainder is: ",result)
res=num1//num2
print("quotient is: ",res)
## Question 7
import math
p=int(input("enter value: "))
r=int(input("enter value: "))
t=int(input("enter value: "))
SI=(p*r*t)/100
print(SI)