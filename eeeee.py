

class xxx:
    def __init__(self):
        self.ab=10
        self.de=12
        self.su = self.sum(self.ab,self.de)
        self.ppt(self.su)
    def sum(self,a,b):
        return a+b
    def ppt(self, sm):
        t=sm*1000
        print(t)
x=xxx()