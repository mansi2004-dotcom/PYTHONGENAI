#Ques1.
def average_marks(*args):
    total=len(args)
    average = sum(args)/total
    for i in args:
        if i>0:
            print(i)
        else:
            print("")
    if i == 0:
        return 0
    else:
        print(i)
    return average
print(average_marks(50,30,80,0,55))

#Ques2.
def filter_details(**kwargs):
    for  keys,value in kwargs.items():
        if type(value) == str:
            print(keys,"=",value)
filter_details(name="mansi" , rollno=1234,marks=34,branch="cse")


