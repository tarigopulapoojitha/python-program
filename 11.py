#program to find sum of factors of given number
class DisplayNumbers:
    def __init__(self):
        self.c=1
        self.s=0
    def accept(self):
        self.n=int(input('enter the n value:'))
    def process(self):
        while self.c<=self.n:
            self.r=self.n%self.c
            if self.r==0:
             print(self.c,end=' ')
             self.s=self.s+self.c
            self.c=self.c+1
        print('\n sum',self.s)
d=DisplayNumbers()
d.accept()
d.process()
            

