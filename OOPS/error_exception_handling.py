#Error and Exception Handling
#Error= Syntax
#Exception = Logical error like Type, Name, Value, Asset

# x=10

# try:
#     print(x)
#     # print(10/0)
#     print(10/2)
# except ZeroDivisionError:
#     print("Zero is not divisible")
# except NameError:
#     print("Variable is not defined")
# except:
#     print("Some Error occurs")
# else:
#     print("No error is occured")
# finally:
#     print("The block is irrespectively")

#Using Class

class Invalidnumber(Exception):
    pass
x=int(input("Enter a no 0 to 10:"))
if 0<=x<=10:
    print("Correct value")
else:
    raise Invalidnumber(f"The {x} value is out of range 0 to 10")
    # print("Wrong Password")

# class Password(Exception):
#     pass
# raise Password("Wrong Password")