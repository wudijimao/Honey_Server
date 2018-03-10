print('Hello World!')

class Test:
    count = 0
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()


