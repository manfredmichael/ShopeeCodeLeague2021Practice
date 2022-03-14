from functools import wraps
from time import time, sleep
import numpy as np
import itertools

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


def calculate_group_noise(employees, l, r):
    group = employees[l: r]
    return sum(group) * len(group)

def calculate_noise(employees, dividers):
    total_noise = 0

    left_divider = 0
    for divider in dividers:
        total_noise += calculate_group_noise(employees, left_divider, divider)
        left_divider = divider
    total_noise += calculate_group_noise(employees, left_divider, len(employees))

    return total_noise

def get_divider_combination(N, k):
    return list(itertools.combinations(range(1, N), k-1))

def bruteforce(employees, k):
    N = len(employees)
    divider_combination = get_divider_combination(N, k)
    noise = [calculate_noise(employees, divider) for divider in divider_combination]
    return min(noise) 

def main():
    result = bruteforce([1, 3, 2, 4], k=2) 
    print(result)

if __name__=='__main__':
    main()
