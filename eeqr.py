class AA:
    def __init__(self):
        self.a1=10
        self.a2=100
    def add(self):
        return self.a1+self.a2


a=AA()
b='a.add()'
c=eval(b)
print(c)