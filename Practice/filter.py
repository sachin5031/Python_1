"""Filter Function
It runs the function in all items in collection manner
but it store true values"""

age =[14,23,45,41,32,7,10,12,20,21,22]

# def adults(x):
#     if x>=18:
#         return True
#     else:
#         return False
# adult=list(filter(adults,age))
# print(adult)

# def adults(x):
#     return x>=18
# adult=list(filter(adults,age))
# print(adult)

adult=list(filter(lambda x : x>18,age))
print(adult)