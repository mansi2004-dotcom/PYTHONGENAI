# dict1={"name": "Mansi","Branch": "Btech","rollno.":1234,23:"twentythree"}
# print(dict1)
# print(dict1.keys())
# print(dict1.get("coder", "not found"))
# for i,j in dict1.items():
#     print(i,"==",j)
# dict2 ={"name":{"firstname":"mansi", "lastname":"Mansi"},"Branch":"Btech","rollno.":1234,
#     "Address":{"permanent":"Pathankot","temp":"Mohali"},"marks":[10,67,90,88]}
# print(dict2["Address"])
# print(dict2["Address"]["temp"])
# dict4={}
# user = int(input("enter numer of times user want  : "))
# for i in range(user):
#     key=input("Enter the key")
#     values=input("Enter the value:")
#     dict4[key]=values
# print(dict4)    

employee_details={
    101:{"name":"Alice","department":"HR","Salary":48000},
    102:{"name":"Bob","department":"IT","Salary":62000},
    103:{"name":"Tom","department":"Finanace","Salary":75000},
    104:{"name":"Sam","department":"Marketing","Salary":50000},
}
salary = []
for i in employee_details.values():
    if i ["Salary"]>50000:
        salary.append(i["name"])
print(salary)