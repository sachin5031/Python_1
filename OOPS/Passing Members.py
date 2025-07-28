#Passing Member

class Engine:

    def __init__(self):
        self.power=100

    def start(self):
        print('Engine is ready to work')

class car:

    def __init__(self):
        self.engine=Engine()

    def move(self):
        self.engine.start()
        print('Car is now ready to move')

c=car()
c.move()