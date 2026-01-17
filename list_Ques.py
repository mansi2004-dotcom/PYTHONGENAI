#Ques1.
# l1=[1,2,3,4,5]
# user=input("enter another friend: ")
# l1.append(user)
# print(l1)
# frd=input("enter most important friend: ")
# loc=int(input("enter location for frd: "))
# l1[loc]=frd
# print(l1)
# #Ques2.
# l2=[1,2,3,4,5,6,7,8,9,10]
# print(l2)
#Ques3.
# l3=[1,10,100,3,6,8]
# l3.insert(2,59)
# print(l3)
# l3.append(5)
# print(l3)
# print(len(l3))
#ques4.
# l4=["Mansi","Tom","Raj","Shreya","Giyan"]
# lc=[i for i in l4 if len(i)<4]
# print(lc)
# #Ques5.
# l5=["Even" if i%2 ==0 else "Odd" for i in range(1,21) ]
# print(l5)
# #Ques6.
# l6=[i for i in range(1,1000) if i%7==0]
# print(l6)
#Ques7.
# string=input("enter a sentence: ")
# # space = [i for i in string if i == " "]
# #print(len(space))
# space = string.count(" ")
# print(space)
l1=["hi l","man  si","me hak"]
l1=[i.count(' ') for i in l1 if ' ' in i]
print(l1)
print(sum(l1))
#Ques8.
la=[1,2,3,4]
lb=[2,3,4,5]
lc=[(i,i) for i in la if i in lb]
print(lc)


    
