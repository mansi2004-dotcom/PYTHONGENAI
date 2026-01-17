##Write a program to check whether a number is positive, negative, or zero.
# n=int(input("enter number: "))
# if n>0:
#     print("number is positive")
# elif n<0:
#     print("number is negative")
# else:
#     print("number is zero")
# ##Ques2.Write a program to reverse a string.
# str1=input("enter a string: ")
# rev_str=""
# for char in str1:
#     rev_str=char + rev_str
# print(rev_str)
##Ques3.Write a program to count the number of digits in a number.
# num=int(input("enter a number: "))
# count=0
# for digit in str(num):
#     count += 1
# print(count)
##  Ques4.Write a program to check if a string is a palindrome.
# string=input("enter string: ")
# rev =""
# for chr in string:
#     rev = chr + rev 
# if string == rev:
#     print("palindrome")
# else:
#     print("Not Palindrome")
##Ques5.Write a program to find the largest of two numbers.
# a= int(input("enter a number: "))
# b=int(input("enter second number: "))
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")
###ques6.Write a program to find the sum of first n natural numbers.
# total =0
# n=int(input("enter number: "))
# for i in range(1,n+1):##n+1 seh hum jitni vlue n ki laingye vahn taak + krke dega.
#     total += i
# print(total)
# ##ques7.Write a program to generate the multiplication table of a number.
# product = 1
# a=int(input("enter a number: "))
# for i in range (1,11):
#     product = a*i
#     print(a ,"*",i,"=",product)
# ##Ques8.Write a program to check whether a number is prime.
# num=int(input("enter number: "))
# if num <= 1:
#     print("False")
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             print("not a prime number")
#             break
#     else:
#         print("prime number")
# ##ques9.Write a program to reverse a number.
# n=int(input("enter a number: "))
# rev = 0
# while n>0:
#     digit = n%10
#     rev = (rev*10 )+ digit 
#     n = n // 10
# print(rev)


#num = "*"
# for i in range(6,0,-1):
#     print(num * i)
#     for j in range(1,6):
# print(num*j)
#Ques.wap to make pattern of K.
# for i in range(6,0,-1):
#     print(num * i)
# for j in range(1,6):
#     print(num*j)

# ##Ques.WAP to print number in pattern.
# n=int(input("enter number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

## Ques.WAP to print the pattern by repeating number.
# m=int(input("enter the rows: "))
# for i in range(1,m+1):
#     for j in range(1,i+1):
#         print(i,end ="")
#     print()
    
for i in range(1,6):
    for j in range(1,i):
        print(j, end=" " )
    print()






    