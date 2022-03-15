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

class Hub:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    result = None
    print(result)

if __name__=='__main__':
    main()
