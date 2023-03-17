#program to find sum of odd numbers in given range
class DisplayNumbers:
    def __init__(self):
        self.s=1
    def accept(self):
        self.i=int(input('enter the initial value:'))
        self.f=int(input('enter the final value:'))
    def process(self):
        while self.i<=self.f:
            self.r=self.i%2
            if self.r!=0:
               print(self.i,end=' ')
               self.s=self.s+self.i
            self.i=self.i+1
        print(self.s)
d=DisplayNumbers()
d.accept()
d.process()
                

