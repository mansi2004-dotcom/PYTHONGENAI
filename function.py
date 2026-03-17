#predefined - print,input
#user - defined
#def - keyword
def sumss():
    print("hello")
    return 'hello'
print(sumss())
def sumss(a,b):
    return a+b

i = int(input("enter i"))
j= int(input("enter j"))
ans = sumss(i,j) # arguments
print(ans)

# functions with default parameters
def multi(a,b=10):
    return a*b
print(multi(34))

#functions with keyword arguments
def printnumber(a,b,c):
    print(a,b,c)

i=10
j=20
k=30
printnumber(i,j,k)
printnumber(c=10,b=20,a=30)

print("----------")
def checkOddEven(a):
    if a%2 ==0:
        return "Even"
    else:
        return "Odd"

n=int(input("Enter Number"))
print(checkOddEven)

print("-----------")
def listSum(l):
    print(l)
    sum =0
    for i in li:
        sum += i
        return sum 
li = [33,56,41,25]
print(listSum(li))
print("--------------------")

# args - keyword argument *a
def sumRet(*a):
    print(a)
    sum =0
    for i in a:
        sum += i
        return sum 
        #return a+b+c
print(sumRet(45,56,88))
print(sumRet(45,56,88,90,100))
print(sumRet(45,56))
print(sumRet(45,56,10,23,56,78,98))

#**kwargs - keyword arbitrary arguments
def sumRet(**a):
    print(a)
    sum =0
    for i in a:
        sum += i
        return sum 
        #return a+b+c
print(sumRet(45,56,88))
print(sumRet(45,56,88,90))
print(sumRet(45,56,))