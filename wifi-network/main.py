from functools import wraps
from time import time, sleep
import numpy as np
from random import randint

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        with open('time_log.txt', 'a+') as file:
            file.write(str(te - ts) + '\n')
        return result
    return wrap

class Engineer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.signal = 0

    def is_inside(self, hub, r):
        return (self.x - hub.x)**2 + (self.y - hub.y)**2 < r**2 


class Hub:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    result = None
    print(result)

if __name__=='__main__':
    main()
