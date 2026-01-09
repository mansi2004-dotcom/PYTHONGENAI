name = input("enter user name: ")
age =int(input("enter user age: "))
ticket_price = input("enter your choice of ticket: ")
if ticket_price == "first":
    print("1500/-")
elif ticket_price == "second":
    print("1000/-")
elif ticket_price == "sleeper":
    print("500/-")
else:
    print("invalid input")
Meal = input("enter yes or no if you want meal: ")
if Meal == "yes":
    print("pay 200 extra")
elif Meal == "no":
    print("No extra charges")

###Ques 2.

print("Welcome to burger king")
menu=input("menu: \n1.whopper burger -rs. 150 \n2.Crispy veg -rs. 100\n3. chicken wings -rs.120\nenter the number(1,2,3): ")
quantity=int(input("enter quantity : "))
coupon =input("do you have a coupon code(yes/no): ")
discount =0
price=0
item=" "
if menu=="1":
    price=150
    item="whopper burger"
elif menu=="2":
    price=100
    item="crispy veg"
elif menu=="3":
    price=120
    item="chicken wings"
total_price=price*quantity
discount_price=0
if coupon =="yes":
    code=input("do you have coupon code?(ys/no): ")
    if code=="KING50":
        discount="50% off"
        discount_price=total_price/2
    elif code=="BK20":
        discount="rs.20 off"
        discount_price=total_price-20
elif coupon =="no":
    code="NOCOUPON"


print("original price",total_price)
print("discount applied",discount)
print("final price",discount_price)
print("hello coder roots")


