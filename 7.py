#program to display odd numbers ini the given range
class DisplayNumbers:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input('enter the n value:'))
    def process(self):
        while self.c<=self.n:
            self.r=self.c%2
            if self.r!=0:
                print(self.c,end=' ')
            self.c=self.c+1
d=DisplayNumbers()
d.accept()
d.process()
                
