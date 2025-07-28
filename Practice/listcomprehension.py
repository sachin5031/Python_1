fruit=["apple","banana","kiwi","mango"]
# new=[]
#
# for x in fruit:
#     if "a" in x:
#         new.append(x)

# new=[x for x in fruit]
# new=[x for x in fruit if "a" in x]
# new=[x for x in fruit if x!="banana"]
# new=[x.upper() for x in fruit]
# new=[x if x!="banana" else "orange" for x in fruit]
# print(new)

#Matrix

# matrix=[]

# for x in range(4):
#     matrix.append(x)
#     print(matrix)

# for x in range(4):
#     matrix.append([])
#     for y in range(4):
#         matrix[x].append(y)
# print(matrix)

# matrix =[[] for x in range(4)]
# print(matrix)


matrix =[[y for y in range(4) ] for x in range(4)]
print(matrix)


matrix1 =[x for x in range(4)]
print(matrix1)