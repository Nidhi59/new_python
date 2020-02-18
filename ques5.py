# ques 5: Python program to form a dictionary from an object of a class.


class Dict1 (object):

    def __init__(self):
        self.A = 1
        self.B = 2


obj = Dict1()
print(obj.__dict__)
