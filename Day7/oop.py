import random
class Ghost(object):
    # your code goes here
    rcolor = ["White","yellow","purple","red"]
    def __init__(self):
        i = random.randrange(0,4,1)
        self.color = self.rcolor[i]