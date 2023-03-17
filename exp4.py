#program to display n numbers
class DisplayNumbers:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input('enter n value:'))
    def process(self):
        while self.c<=self.n:
              print(self.c,end=' ')
              self.c=self.c+1
d=DisplayNumbers()
d.accept()
d.process()
