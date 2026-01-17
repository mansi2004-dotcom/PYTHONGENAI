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