#Polymorphism- Overloading and Overriding

# Overloading

# def f1():
#     print("One")
# def f1():
#     print("Two")
# def f1():
#     print("Three")

# f1()

#overriding
def mul(x,y=None,z=None):
    if y and z:
        print(x*y*z)
    elif y:
        print(x*y)
    else:
        print(x)

mul(10)
mul(10,20)
mul(10,20,30)

# Duck Typing (It cannot check what kind of data is given and it give value what we inserted)

def add(a,b):
    return  a+b

print(add(10,20))
print(add("Hello ",'World'))