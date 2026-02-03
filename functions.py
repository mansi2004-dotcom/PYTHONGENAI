# ## functions ka hum use isliye krte hai like humne 2student ki average nikalni hai tuh hum stu1 ki 
# ##average nikalenge fir 2 ke liye nikalegye per agar 10 ka nikalna ho tuh bhut tough hai baar baar 
# ## krna. islye hum function ka use krte hai.
# stu_1=[50,60,70]
# total=sum(stu_1)
# count=len(stu_1)
# average=total/count
# print("Average of student 1 is ",average)
# stu_2=[40,60,90]
# total=sum(stu_2)
# count=len(stu_2)
# average=total/count
# print("Average of student 2 is ",average)
# ## Abh function bnanae ke liye hum use krte hai def ko. def mai hum function ka name use krte hai
# #or usme pass krte hai parameters. abh function ko banane ke baad usse call bhi krna padhta hai aese vo
# # kuch bhi print nhi krega.
# def sum(a,b): # a,b is parameters
#     c=a + b
#     print("sum of a,b is ",c)
# sum(11,34) #11,34 is arguments
# sum(45,78)
# function ko hum baar baar use kr skte hai. 
## return function 
# def multi(a,b):
#     n=a*b
#     return f"The product is {n}"# only written this line will not show the ans on console window.so,
#     # we have to store func in another variable then print them.
# s=multi(8,9)
# print(s)


# # ##Local Variable
# def xyz(a,b):
#     a=20
#     b=30
#     c=a*b
#     print(c)   
#     print(a,b) # it does not print the value of a and  b bcz local variable does not call outside the 
# # #     function.
# xyz(4,5)
    
# m= xyz(10,20)
# print(m)## it print 600 bcz we already defne the value of a and b.

# def odd_eve():
#     A=int(input("enter a: "))
#     if A%2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#         return A
# odd_eve()

# def x():
#     x=int(input("enter number : "))
#     for i in range (0,x+1):
#         for j in range(i):
#                 print("*",end=" ")
#         print()
# x()
# ##For square pattern
# def num():
#     num = int(input("enter number: "))
#     for i in range(num+1):
#         for j in range(num):
#             print("*",end=" ")
#         print()
# num()
# ##For reverse pattern
# def n():
#     n=int(input("enter num: "))
#     for i in range(n,0,-1):
#         for j in range(i):
#             print("*",end=" ")
#         print()
# n() 
##paramid pattern 
def pat():
    pat = int(input("enter a: "))
    for i in range(1,pat+1):
        for j in range(""*(pat-i) + "*" *i):
            print("*",end ="")
        print()
pat()


    

