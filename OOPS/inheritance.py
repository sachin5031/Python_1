#Inheritance
#Single Level
#Multiple Level
#Multi Level
#Hierarchy Level

#Single Level

# class A:
#     def A(self):
#         print('I am A')
#
# class B(A):
#     def B(self):
#         print('I am B')
#
# obj = B()
# obj.B()

#Multiple Level

# class A:
#     def A(self):
#         print('I am A')

# class B:
#     def B(self):
#         print('I am B')

# class C(A,B):
#     def C(self):
#         print('I am C')

# obj = C()
# obj.A()
# obj.B()
# obj.C()

# # Multi Level

# class A:
#     def A(self):
#         print('I am A')
# class B(A):#A,B
#     def B(self):
#         print('I am B')

# class C(B): #A,B,C
#     def C(self):
#         print('I am C')

# obj = C()
# obj.A()
# obj.B()
# obj.C()

# Hierarchical Level

class A:
    def A(self):
        print('I am A')
class B(A):#A,B
    def B(self):
        print('I am B')

class C(A): #A,C
    def C(self):
        print('I am C')

class D(A): #D,C
    def D(self):
        print('I am D')

obj = D()
obj.A()
obj.D()