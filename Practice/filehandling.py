# File handling in Python
# opening a file = open()
# Modes of opening a file:
# "r" - read
# "w" - write
# "a" - append
# "x" - exclusive creation (fails if file exists)

# f = open("new.txt","r")
# print(f.read())
# f.close()

# f = open("new.txt","r")
# # print(f.read(21))
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f = open("new.txt","w")
# f.write("This is new line")
# f.close()
#
# f = open("new.txt","r")
# print(f.read())

# f = open("new.txt","a")
# f.write("This is new line")
# f.close()
#
# f = open("new.txt","r")
# print(f.read())

# f=open("car1.txt","w")

import os
# os.remove("car.txt")
# os.remove("file.txt")

if os.path.exists("car.txt"):
    os.remove("car.txt")
else:
    print("file not found")