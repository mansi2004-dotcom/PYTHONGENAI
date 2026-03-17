a = int(input("Enter a number: "))
product = 1
for i in range(1,11):
    product = a*i 
    print(i,"*",a,"=",product)

#ques2:
num = int(input("enter a number: "))
if num>1:
    for i in range(2,num):
        if num %i == 0:
            print("not prime number")
            break
    else:
        print(" prime number")

dict1 = {"name1":"kirtika","name2":"Mansi","name3":"Priya","name4":"Palvinder"}
print(dict1["name4"])
student = {"name":"Mansi","Branch":"CSE","RollNo.":23}
student["course"] = "Btech"
print(student)
