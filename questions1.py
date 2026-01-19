##Ques1.
# for i in range(0,51):
#     if i%3==0 and i%5 == 0:
#         print("fizzbuzz")
#     elif i%5 == 0:
#         print("buzz")
#     elif i %3 == 0:
#         print("fizz")
#     else:
#         print(i)
##Ques2.
# for n in range(2, 101):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         print("pime number", end=" ")
#     else:
#         print(i,end =",")
##Ques3.
# num = int(input("enter a score between 1 to 100 : "))
# if num >=90 and num <100:
#     print("A grade")
# elif num >=80 and num <89:
#     print("B grade")
# elif num >=70 and num<79:
#     print("C grade")
# elif num>=60 and num<69:
#     print("D grade")
# elif num<60:
#     print("Fail") 
# ##  Ques4.
# num1=int(input("enter a number: "))
# for i in range (1,11):
#     print(num1,"*",i,"=",i*num1)
# ##Ques5.
# lc=[i**2 for i in range(21) if i%2 == 0]
# print(lc)
##Ques 6.
# year = int(input("enter a year: "))
# if year %4 == 0:
#     print("leap year")
# elif year % 400 == 0:
#     print(" leap year")
# elif year % 100 !=0:
#     print("not leap year")
# ##Ques7.
# side1 = int(input("enter  length of triangle: "))  
# side2 = int(input("enter  length of triangle: "))  
# side3 = int(input("enter  length of triangle: "))  
# if side1 == side2 == side3:
#     print("Equilateral triangle")
# elif side1 == side2:
#     print("Isosceles")
# else:
#     print("Scalene ")
#ques.8
# num2=int(input("enter a number: "))
# if num2>0 :
#     print("positive")
# elif num2<0:
#     print("negative")
# else:
#     print("Zero")
# #Ques9.
# BMI=float(input("enter body mass index:  "))
# if BMI < 18.5:
#     print("Underweight")
# elif BMI <= 24.9:
#     print("Normal weight")
# elif 25 <= BMI <29.9:
#     print("Overweight")
# elif BMI >= 30:
#     print("Obesity")
#Ques10
# day = int(input("enter day : "))
# if day == 1:
#     print("Monday")
# elif day ==2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("thursday")
# elif day ==5:
#     print("Friday")
# elif day ==6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# #ques11.
# sum = 0
# num3=int(input("enter number: "))
# for i in range(0,num3+1):
#     sum += i
# print(sum)
# #ques12.
# price = int(input("enter a price: "))
# discount = 0
# if price> 1000:
#     discount = 0.9
#     print(discount*price)
# elif price >500 and price < 1000:
#     discount = 0.95
#     print(discount*price)
# elif price >500:
#     print(price)
# #ques13.
# count = 0
# vowel =  "aeiouAEIOU"
# srt=input("enter a string : ")
# for char in  srt:
#     if char in vowel:
#         count += 1
# print("total vowel: ",count)
# #ques14.
# total =0
# num4=int(input("enter n number: "))
# for i in range(0,num4+1):
#     total +=i
# print(total)
# n = int(input("enter n : "))
# for i in range(0,n):
#     for j in range(0,i):
#          print("*",j)
# #Ques15.
# use=int(input("enter number: "))
# for i in range(0,use):
#     if i%2 == 0:
#         print(i)
#Ques16.
# count =0
# l=[11,25,34,78,76,89,90,45,88,90]
# if 25 in l:
#     print("it exist")
# else:
#     print("not exist")
# print(len(l))
# print()
# print("total number of occurrence of 25 is :",l.count(25))
# for element in l:
#     if element%2 == 0:
#         print(element)
        
# ##Ques17.
str2=input("enter string min 10 words and max 19 words: ")
count_str2=len(str2)
if 10 <= count_str2 <=19:
    print(str2)
    print(len(str2))
else:
    print("not")
if str2 == str2[::-1]:
    print("palindrome")
else:
    print("not palindrome")
print("second last word in string: ",str2[-2])
middle=count_str2//2
print("middle word in string: ",middle)

# ##ques18.
# print("Welcome to Calci:\n1. Power\n2. Sum\n3.Sub\n4.Multiple")
# choice =input("enter your choice: ")
# sum1=int(input("enter first number to sum: "))
# sum12=int(input("enter second number to sum: "))
# sum = sum1 + sum12
# print(sum)
##Ques 19.
# comp_num=int(input("enter a number between 1-100: "))
# user_num=int(input("guess a number between 1-100: "))
# if comp_num == user_num:
#     print(comp_num)
# else:
#     print("not found")

##Ques20.
count = 0
input1=["aba","abc","1221",'123321']
for i in input1:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
        
print(count)





