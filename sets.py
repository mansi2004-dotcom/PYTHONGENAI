##sets -{} , heterogeneous, unique elements,unordered.
#it does not take repeated values. pop function in set it delete any value.in remove function we have to give value in set.otherwiise give error.
##discard function does not rais error if value is not present.
set1={22,45,"hi",True,"surbhi",45,100}## it give o/p in not same order but in different order.
print(set1)
set1.add(55)
print(set1)
set1.update({33,67,220})
set1.update([33,67,220])
print(set1)
set1.pop()
print(set1)
set1.remove(220)
print(set1)
set1.pop()# pop first element in the set.
print(set1)
set1.discard(45)
print(set1)
##frozen set
s=frozenset(["a","b","c","d"])
print(s)
Marketing={"photoshop","slack","zoom","canva","trello"}
sales_uses={"salesforce","slack","zoom","linkedin","hubspot"}
result = Marketing.intersection(sales_uses)
print(result)
unique=Marketing.union(sales_uses)
print("company footprint: ",list(unique))
setA=Marketing.difference(sales_uses)
print("specialized tool:",setA)
setB=Marketing.symmetric_difference(sales_uses)
print(setB)
universal_license={"slack","zoom"}
setC=universal_license.issubset(Marketing)
print(setC)
n=int(input("enter number: "))
factorial=1
for i in range(1,n+1):
    factorial *= i
print(factorial)
##AArgs
def sumRet(*a):
    print(a)
    sum =0
    for i in a:
        sum +=i
        return sum
        return a+b+c