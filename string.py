name = "Mansi"
print(len(name))
print(name[3])
# index slicing

print(name[:])# start,stop,step
print(name[0:4])
print(name[:5])
print(name[1:])
print(name[:20])
print(name[1:6:-1])#print empty 
print(name[6:1:-1])#print reverse

#Methods
print("---------------------")
print(name)
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.swapcase())
print(name.endswith("si"))#give ans in boolean check is end with si or not.it is case sensitive.
print(name.startswith("ma"))#check is strin start with ma or not.it is case sensitive.

print("---------------------")
str1="     hello  hi   "
print(str1.strip())# remove extra space from both side.
print(str1.lstrip())# remove extra space from left side.
print (str1.rstrip())#remove extra space from right side.

print("---------------------")
n="himanshu dhiman"
print(n.replace("an","u"))

print("--------------------")
i="hello , how are you class"
print(i.split())
print(i.split("o"))

name = input("enter name: ")
for i in name:
    print(name,i)