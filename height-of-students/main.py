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
    return list(map(int, input().split()))

def read_one_str():
    """ Input parser for one string """ 
    return int(input())

def read_multi_str():
    """ Input parser for multiple string """ 
    return input().split()

def get_diff(t):
    return [j-i for i, j in zip(t[:-1], t[1:])] 

def get_sad_students(diffs):
    return sum([1 for i in diffs if i < 0]) 

def func1 (Height):
    sad_combinations = []
    for i in range(len(Height)):
        new_order = Height[0:i] + Height[i+1:len(Height)] + [Height[i]]
        diff = get_diff(new_order)
        sad_count = get_sad_students(diff)
        if sad_count == 0:
            return 0
        sad_combinations.append(sad_count)
    return min(sad_combinations)

T = read_one() 
for _ in range(T):
    N = read_one() 
    heights = read_multi() 

    out_ = func1(heights)
    print (out_)
