# #Ques1.
# friday={"Alice","Bob","Charlie"}
# saturday={"Charlie","David","Eve"}
# all_guests=friday.intersection(saturday)
# allGuest=friday.difference(saturday)
# print(all_guests)
# print(allGuest)
# #Ques2.
# duplicates=[1,2,2,3,4,4,4,5]
# sets=set(duplicates)
# sets.add(6)
# print(sets)
# #Ques3.
# lib_books={"Hobbit","1984","Gatsby","odyssey","hamlet"}
# checked_out={"1984","hamlet"}
# available=lib_books.difference(checked_out)
# print(available)
# lib_books.update({"Don Quixote"})
# print(lib_books)
# #Ques4.
# user_permission={"read","write"}
# admin_reqs={"read","write","execute"}
# result=user_permission.issubset(admin_reqs)
# specific_perm=admin_reqs.difference(user_permission)
# print("specific permission user missed",specific_perm)
# print("is the user set is subset of requirementd:",result)
# #Ques5.
# logs={
#     "404":[10,12,15,20],
#     "500":[12,20,22,25],
#     "403":[10,20,30]
# }
# sets1=set(logs["404"])
# sets2=set(logs["500"])
# sets3=set(logs["403"])
# error_server=sets1 & sets2 & sets3
# print(error_server) 
# critical_server=sets2.difference(sets1)
# print(critical_server)
