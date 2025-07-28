#Encapsulation

class car:
    __price=5000
    def display_price(self):
        print(f'{self.__price}, this is the price of car')

c1=car()
c1.display_price()