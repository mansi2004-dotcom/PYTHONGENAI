#Write a program to find the length of a list.
li=["hi","Mansi","tom","radha","sima"]
print(len(li))
#Write a program to find the sum of all elements in a list.
l=[1,2,3,4,5,6,7,8,9]
total=0
for i in l:
    total += i
print(total)
#Write a program to find the largest and smallest number in a list.
l1=[11,3,22,56,24,78,45,12,2,56,7,9,13]
# max1 = l1[0]
# min1= l1[0]
# for i in l1:
#     if i>max1:
#         max1 = i
#     if i<min1:
#         min1 = i
# print("max",max1)
# print("min",min1)
maxi = l1[0]
mini = l1[0]
for i in l1:
    if  i>maxi: 
        maxi = i
    elif i<mini:
        mini = i
print("max",maxi)
print("min",mini)
## Write a program to find the sum of all elements in a list.
ele=[1,2,3,4,5,6,7]
total = 0
for i in ele:
    total += i
print(total)
##Count how many times a given element appears in a list.
lis=[2,3,45,5,2,4,5,6,2]
for i in lis:
    if i == i:
print(lis)
    else:
        print("not similar")




