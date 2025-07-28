list = ["Car","Bus","Bike"]

# def key(list): #def key(x)
#     print(list*3)#print(x*3)
# key(list)#key(x)

def loop(x):
    print(x*3)

def map(crazy,list):
    for i in list:
        crazy(i)

map(loop,list)

# List
# list = ["Car","Bus",3,5.0,56,3,True]

# print(len(list))
# print(type(list))
# print(list[2])
# print(list[2:5])
# list[2]="jeep"
# print(list)
# list[1:3]="jeep","bus"
# print(list)
# list.insert(3,"oranges")
# print(list)
# list.append("oranges")
# print(list)

#Tuple
# t1 = ["Car","Bus",3,5.0,56,3,True]
# x = list(t1)
# x[2]="balloon"
# y = tuple(x)
# print(y)

