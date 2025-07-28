#Class Methods

class student:
    school_name="KCS School"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f'Name:{self.name}, Age:{self.age}')

    @classmethod
    def get_schnmae(cls):
        return cls.school_name

    @staticmethod
    def is_adult(age):
        return age>=18

x=student('Sachin',21)
x.display()
print(x.get_schnmae())
print(x.is_adult(11))
print(x.is_adult(x.age))
print(student.is_adult(12))
print(student.is_adult(22))