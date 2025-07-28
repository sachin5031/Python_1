#Decorator (It returns the wrapping content using '@'method)

# def my_deco(fun):
#     def wrapper():
#         print("Some thing happened BEFORE function")
#         fun()
#         print("Some thing happened AFTER function")
#     return wrapper
#
# def say_hello():
#     print("Hello Sachin")
#
# decorator=my_deco(say_hello)
# decorator()

# @my_deco
# def say_hello():
#     print("Hey Sachin")
# say_hello()

#Generator(Passes value by using 'yield' key word)

# def gen():
#     yield 1
#     yield 2
#     yield 3

# for x in gen():
#     print(x)
#     print(x,"The value of x")
#     print(x,'This is generator')
#     print('==============')

# x = gen()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x)) #iteration would be stopped bcz limit is 3

#Fibonacci series
def fibo(limit):
    a,b=0,1
    while a<limit:
       yield a
       a,b =b,a+b
x = fibo(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x)) #iteration would be stopped bcz limit is 5 so the no of 3 doesnt go to another step
# bcz next iteration is 3+2 is 5 so 5 is equla but not smaller than limit

# for x in fibo(100):
#     print(x) # after 89 next itr wouldnt print bcz 89+55 is 144 so it is out of range for 100

# def mk(x):
#   def mk1():
#    print("Decorated")
#    x()
#    print("Decorated")
#   return mk1
#
# # def mk2():
# #  print("Ordinary")
# # p = mk(mk2)
# # p()
#
# @mk
# def mk2():
#   print("Ordinary")
# mk2()