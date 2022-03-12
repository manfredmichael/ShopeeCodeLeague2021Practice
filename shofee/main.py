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

def get_valid_combination_count(beans, k, n=1, previous_sum=0):
    if n > len(beans):
        return 0
    
    current_sum = (previous_sum + beans[n-1])
    mean = current_sum/n
    if mean >= k:
        return 1 + get_valid_combination_count(beans, k, n+1, current_sum)
    else:
        return 0 + get_valid_combination_count(beans, k, n+1, current_sum)

@timing
def get_total_valid_combination(beans, k):
    c = [get_valid_combination_count(beans[i:], k, n=1) for i in range(len(beans))]
    return sum(c)

def main():
    test_case = [1, 1, 4, 5, 1, 4] * 1000
    result = get_total_valid_combination(test_case, 3)
    print(result)

if __name__ == '__main__':
    main()
