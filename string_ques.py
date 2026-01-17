#ques1.
name ="coder roots"
print(name[0:2]+ name[-2:])
name1="New Year"
print(name1[0:2] + name1[-2:] )
if len(name)<2 and len(name1)< 2:
    print("invalid string")
else:
    print("valid string")

#Ques2.
str1="Coder"
str2="roots"
print(str1.split() + str2.split())
print(str1.replace("C","r")+ " " +  str2.replace("r","C"))
#Ques3.
string = "coder roots"
print(string[:6] + string[6+1:])
# Ques4.
string = input("enter string: ")
len_str = len(string)
if  len_str<3:
    print("string")
elif string.endswith("ing"):
    print(string + "ly")
else:
    print(string +"ing")
