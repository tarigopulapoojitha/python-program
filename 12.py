class DisplayNumbers:
    def __init__(self):
        self.s=0
    def accept(self):
        self.n=int(input('enter the n value:'))
    def process(self):
        while self.n>0:
            self.r=self.n%10
            self.s=self.s+self.r
            self.n=self.n//10      
        print(self.s,end=' ')
d=DisplayNumbers()
d.accept()
d.process()
            

