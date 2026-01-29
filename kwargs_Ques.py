# def add_num(*args):
#     return sum(args)
# print(add_num(1,2))
# print(add_num(1,2,3,4))
# def numAdd(*a):
#     s= sum(a)
#     return s
#     # for i in a:
#     #     s += i
#     #     return s
# print(numAdd(4,6))
#Add using args
# def addNum(*args):
#     return sum(args)
# print(addNum(12,23))
#Ques. kwargs sum

def filter_details(**kwargs):
        print( sum(kwargs.values()))
filter_details(Name=30, Branch=70, Rollno= 12)