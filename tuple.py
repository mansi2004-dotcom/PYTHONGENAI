#tuple - (),ordered,indexed based,immutable(cannot changed during run time)
t=[]
print(t)
s=(12) # if we write only 12 without comma then it print int .so, we must put the comma(,)at end for tuple.
print(type(s))
#we can do slicing in it .
a=(1,4,56,78,88,6,64)
print(a[1::-1])
#change tuple 
a=list(a)
a[3]=100
a=tuple(a)
print(a)
print(type(a))
l =[13]
print(type[l])
t = (12,)# tuple , without comma isski daatype joh hai wahi rhegyi
print(type(t))
t1 = (12,'hello',True,7.89,22,11,10)
print(t1)

#slicing
print(t1[:])
print(t1[1:5])
print(t1[1:5:2])
print(t1[1::-1])

# 'tuple' object does not support item assignment
# t1[2]= 10
t1=list(t1)
t1.insert(2,350)
t1=tuple(t1)
print(t1)