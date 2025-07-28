#Inner Class

class Outer:
    def __init__(self):
        self.x=10

    class Inner:
        def __init__(self):
            self.y=20
        def in_display(self):
            print('Inner Clasd')

    def out_display(self):
        print('Outer Class')

out=Outer()
in_=out.Inner()