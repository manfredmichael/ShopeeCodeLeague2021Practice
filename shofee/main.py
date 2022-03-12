from functools import wraps
from time import time, sleep
import numpy as np

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

def get_valid_combination_count(beans, n, k):
    valid_combination_counter = 0
    for i in range(len(beans)-(n-1)):
        combination = beans[i:i+n]
        if sum(combination)/len(combination)>=k:
            valid_combination_counter += 1 
    return valid_combination_counter

@timing
def get_total_valid_combination(beans, k):
    return sum([get_valid_combination_count(beans, n, k) for n in range(1, len(beans)+1)])

def main():
    test_case = [1, 1, 4, 5, 1, 4] 
    result = get_total_valid_combination(test_case, 3)
    print(result)

if __name__ == '__main__':
    main()




