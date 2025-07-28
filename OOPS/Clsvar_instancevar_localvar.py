# Class Variable, Instancse variable, Local variable

class customer:
    bank_name="HDFC Bank"         #Class Variable

    def __init__(self,name,age,init_balance):
        self.name=name
        self.age=age            #Instance Variable
        self.balance=init_balance
        
    def deposit(self,amount):
        self.balance += amount        #local Variable
        print(f"The deposit of Rps.{amount} is successful.Updated balance is {self.balance}")

c1=customer("Sachin",21,50000)
print(c1.name)
print(c1.age)
print(c1.balance)

c1.deposit(1000)

c2=customer("Bharath",20,4000)
print(c2.age)
print(c2.name)
print(c2.balance)

c2.deposit(5000)