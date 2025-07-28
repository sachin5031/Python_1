# a=[12,'a',34,True,'sachin']
# print(a)
# b =list(range(10))
# print(b)
# c =list(range(1,10,2))
# print(c)

#List methods

# l1=['Apple',"Cherry",'Pineapple','Banana','watermelon','apple']
# l2=l1.copy()
# print(l1)
# print(l1.index("Cherry"))
# print(l1.count("Cherry"))
# l1.reverse()
# print(l1)
# l1.sort()
# print(l1)
# l1.sort(key=str.lower)
# print(l1)
#
# print(l1)
# print(l2)
#
# del l1[1]
# print(l1)
# print(l1)
# print(l2)
#
# l1.clear()
# print(l1)
# print(l2)

#Max, Min

l1=[12,34,55,77,90,21,-11]
# print(max(l1))
# print(min(l1))

#Membership

print(55 in l1)
print(56 in l1)
print(55 not in l1)
print(56 not in l1)

#Nested list
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[12,13,14]

# l1.append([10,11,12])
# print(l1)
#
# l1.append(l2)
# print(l1)

l1.extend(l2)
print(l1)

print(l1[2][1])

