# # # ques1.
# # a = int(input("enter a number: "))
# # if a%2 == 0:
# #     print("Even Number")
# # else:
# #     print("Odd Number")
# #ques2.
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)
# a =int(input("enter a: "))
# b = int(input("enter b : "))
# c = int(input("enter c: "))
# if a > b and a>c:
#     print("a is the largest number")
# elif b>a and b>c:
#     print("b is largest")
# elif c>a and c>b:
#     print("c is largest")

# a = {1,2,34,6,7,3,67}
# b = {1,6,7,88,23,64,67}
# print(a.intersection(b))
# print(a.union(b))
# print(a.issubset(b))
# print(b.issubset(a))
# lt = [1, 2, 3]
# lt.insert(10, 5)
# print(lt)
# #Ques->
# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# if num1 > num2:
#     for i in range(5):
#         i = "Mansi"
#         print(i)
# else:
#     for i in range(3):
#         i = "Singh"
#         print(i)
# #Ques ->
# st1 = input("enter first string: ")
# st2 = input("enter second string: ")
# st3 = int(st1)
# st4 = int(st2)
# if st3 is st4:
#     print("Both are Equal")
# else:
#     print("Not Equal")

#Ques ->
# user = int(input("enter a number: "))
# for i in range(0,user):
#     if i%2 == 0:
#         print(i,end=",")
#Ques ->
n=4
for i in range(1,n+1):
    print(" "*(n-i),end = "")
    print("* "*i)  
for i in range(n,0,-1):
    print(" "*(n-i),end = "")
    print("* "*i)
#Ques ->
# n=4
# for i in range(n,0,-1):
#     print(" "*(n-i),end = "")
#     print("* "*i)

#Ques ->Prime Number
num=int(input("Enter a Number: "))
if num <= 1:
    print("Not Prime Number")
else:
    for i in range(2,num):
        if num%i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")


