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
max1 = l1[0]
min1= l1[0]
for i in l1:
    if i>max1:
        max1 = i
    if i<min1:
        min1 = i
print(max1)
print(min1)
    



