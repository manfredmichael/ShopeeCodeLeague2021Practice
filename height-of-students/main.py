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


def read_one():
    """ Input parser for one integer """ 
    return int(input())

def read_multi():
    """ Input parser for multiple integer """ 
    return map(int, input().split())

def read_one_str():
    """ Input parser for one string """ 
    return int(input())

def read_multi_str():
    """ Input parser for multiple string """ 
    return input().split()

def func1 (Height):
    pass

T = read_one() 
for _ in range(T):
    N = read_one() 
    heights = read_multi() 

    out_ = func1(heights)
    print (out_)
