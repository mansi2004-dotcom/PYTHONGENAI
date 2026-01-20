#Write a program to find the length of a list.
# li=["hi","Mansi","tom","radha","sima"]
# print(len(li))
# #Write a program to find the sum of all elements in a list.
# l=[1,2,3,4,5,6,7,8,9]
# total=0
# for i in l:
#     total += i
# print(total)
# #Write a program to find the largest and smallest number in a list.
# l1=[11,3,22,56,24,78,45,12,2,56,7,9,13]
# # max1 = l1[0]
# # min1= l1[0]
# # for i in l1:
# #     if i>max1:
# #         max1 = i
# #     if i<min1:
# #         min1 = i
# # print("max",max1)
# # print("min",min1)
# maxi = l1[0]
# mini = l1[0]
# for i in l1:
#     if  i>maxi: 
#         maxi = i
#     elif i<mini:
#         mini = i
# print("max",maxi)
# print("min",mini)
# ## Write a program to find the sum of all elements in a list.
# ele=[1,2,3,4,5,6,7]
# total = 0
# for i in ele:
#     total += i
# print(total)
##Count how many times a given element appears in a list.
# lis=[2,3,45,5,2,4,5,6,2]
# for i in lis:
#     if i == i:
#         print(lis)
#     else:
#         print("not similar")

##Check whether a given element exists in a list.
# l1=[22,45,67,33,56,89,55,12,33,45,66,90]
# element1=55
# if element1 in l1:
#     print("element is exist")
# else:
#     print("element not exist")  
# ##Find the sum of all elements in a list.
# total = 0
# list1 =[2,3,4,5,6,7]
# for i in list1:
#     total += i
# print(total)
##Find the largest and smallest element in a list.
list2=[23,5,34,78,55,24,1]
largest = max(list2)
smallest = min(list2)
print("largest number: ",largest)
print("smallest number: ",smallest)
##Print elements at even indices of a list.
list_1=[12,23,45,66,111,67,89]
print(list_1[::2])
##Swap the first and last elements of a list.
list_2=[11,43,7,33,22,6,89]
print([list_2[0]] + list_2[-1])


