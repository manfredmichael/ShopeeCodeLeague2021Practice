from functools import wraps
from time import time, sleep
import numpy as np

import sys
sys.setrecursionlimit(100_000)
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

def main():
    pass

if __name__=='__main__':
    main()
