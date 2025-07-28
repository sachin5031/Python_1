""""Map Function
It runs the function in all items in collection manner
"""
coll1=[10,20,30,40,50,70]
# coll2=[]

#Using for condition method
# for x in coll1:
#     coll2.append(float(x))
# print(coll2)

# coll2=list(map(float,coll1))
# print(coll2)

coll2=list(map(lambda x : x*2,coll1))
print(coll2)
