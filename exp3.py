#program to display vandemataram n times
class DisplayNtimes:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input('enter a number to display:'))
    def process(self):
        while self.c<=self.n:
              print('vanddemataram#',self.c)
              self.c=self.c+1
d=DisplayNtimes()
d.accept()
d.process()
