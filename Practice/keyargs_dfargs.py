#arbitarary arguments and *agrs(It returns the multiple values)

# def arg(*name):
#     print('Hello',name)
#
# arg('a','b','c','d')
# arg('a','b','c','d','e','f','g')

# def arg(*name):
#     for each in name:
#       print('Hello',each)
#
# arg('a','b','c','d')
# arg('a','b','c','d','e','f','g')

#key = values

# def no(x,y):
#     print(x)
#     print(y)
#     print(x+y)
# no(y=30,x=40)

#arbitarary key arguments and **keyargs(It return the multiple data values)

# def value(**details):
#     print(details)
# value(name='Sachin',id=5031,age=21,city='Chennai') #It prints the values in dictionary values

def value(**details):
    for key,value in details.items():
      print(key,value)
value(name='Sachin', id=5031, age=21, city='Chennai')