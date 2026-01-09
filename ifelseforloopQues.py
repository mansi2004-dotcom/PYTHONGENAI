#Ques1.
# month=["invalid month","january","feburary","march","april","may","june","july","august","september","october","november","december"]
# a=int(input("enter number (1-12): "))
# if 1<= a <= 12:
#     month_name = month[a]
#     print(month_name)
# else:
#     print("invalid number")
# #Ques2. Part1
# num1 =int(input("enter a number: "))
# num2 =int(input("enter second number: "))
# if num1 == num2:
#     print("both number are equal") 
# else:
#     print("both number are not equal")
# ##part2
# if num1> num2:
#     print("first number is greater",num1)
# else:
#     print("second number is greater",num2)
# ##part3
# if num1<num2 :
#     print("num1 is smaller")
# else:
#     print("num1 is equal to num2")
# ##part4
# if num1>num2:
#     for i in range(1,6):
#         print("Mansi")
# elif num1<num2:
#     for i in range(1,4):
#         print("Singh")
#Qus3
# str1=input("enter str1: ")
# str2=input("enter str2: ")
# if str1 == str2:
#     print("both string is equal")
# else:
#     print("strings are not equal")
# ###part2
#     print("strings are equal",str1 is str2)
##ques4
# user1=input("enter str1: ")
# user2=input("enter str2:" )
# input1=int(user1)
# input2=int(user2)
# if(input1 is input2):
#     print("both are equal")
# else:
#     print("both are not equal")

##Ques5
# sum=0
# for i in range(1,8):
#     sum += i
#     print(sum)
##ques6
num=int(input("enter a number: "))
for i in range(0, num):
    i += 1
    if i%2==0:
        print(i)

##Ques7
digit1=int(input("enter a number: "))
op=input("enter operator + or -: ")
if op == "+":
    for i in range(0,digit1):
        i += 1
        print(i, end=",")
elif op == "-":
    for i in range(digit1,0,-1):
        print(i, end=",")


    