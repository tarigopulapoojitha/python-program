#program to read a number and check whether it is divisible by 2 and 5
class DisplayNumbers:
    def accept(self):
        self.n=int(input('enter the n value:'))
    def process(self):
        self.r=self.n%2 or self.n%5
        if self.r==0:
            print(' divisible')
        else:
            print(' not divisible')
d=DisplayNumbers()
d.accept()
d.process()
        
        
