#Constructor

# class parent:
#     def __init__(self,age,name):
#         self.name=name
#         self.age=age

# class child(parent):
#     def __init__(self,name,age,school):
#         parent.__init__(self,name,age)
#         self.school=school

# obj=child('Sachin',21,'KCS School')
# print(obj.name)
# print(obj.age)
# print(obj.school)

#Super() (Super key word is used to merge in the child class and we cannot use the self method in child class)

class parent:
    def __init__(self,age,name):
        self.name=name
        self.age=age
class child(parent):
    def __init__(self,name,age,school):
        super().__init__(name,age)
        self.school=school

obj=child('Sachin',21,'KCS School')
print(obj.name)
print(obj.age)
print(obj.school)