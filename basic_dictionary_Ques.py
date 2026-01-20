# dict3={}
# n=int(input("enter number of items: "))
# for i in range(n):
#     key=input("enter key: ")
#     value=input("enter value: ")
#     dict3[key]=value
# print(dict3)
##Create and print a dictionary.
# d={"name":"Shalini","Branch":"CSE","college":"SBssu"}
# print(d)
##Take dictionary input from user and print it.
# d1={}
# dict_1=int(input("enter number of items: "))
# for i in range(dict_1):
#     keys=input("enter keys: ")
#     values=input("enter values: ")
#     d1[keys]=values
# print(d1)
##Access a value using a key.
el={"name":"Mansi","Branch":"CSE","URN":1234}
# print(el.get("Branch")) # or print(el["Branch"])
# ##Check if a key exists in dictionary.
# print(el.get("coder","not found")) # or
# d={"int":23,"num":34}
# key=input("enter key: ")
# if key in d:
#     print ("exist")
# else:
#     print("not exist")
print(el.items())