##wap to check whether the number is prime or not.
# n=int(input("enter a number:"))
# print(n**0.5)
# if n<=1:
#     print("False")
# else:
#     prime = True
#     for i in range (2,n):
#         if n%i==0:
#             prime = False
# print(prime)

##check whether the number is palindrome or not.
# num = input("enter a number : ")
# if num == num[::-1]:
#     print("palindrome")
# else:
#     print("not")

n= int(input("enter number: "))
rev=0
temp=n
while n>0:
    rev=(rev*10)+n%10
    n=n//10
if temp == rev:
    print("Palindrome")
else:
    print("not Palindrome")

#print number 1 to 100:
#if divisibel by 3:print fizz   if by 5:printbuzz   if by both:print fizzbuzz
# for i in range (1,101):
#     print(i,end=",")
# num = int(input("enter number: "))
# if num%3 ==0 and num%5 ==0:
#     print("FizzBuzz")
# elif num%5 ==0:
#     print("Buzz")
# elif num%3 ==0:
#     print("fizz")
# else:
#     print("False")
    


