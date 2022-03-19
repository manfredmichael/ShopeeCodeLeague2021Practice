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

def find_all_grounds(terrain):
    ground_ids = [i for i, v in enumerate(terrain) if v == 1]
    return ground_ids

def search(terrain, position, step):
    highest_id = None

    while True:
        highest_id = position
        if can_step_to(terrain, position, position + step):
            position += step
        else:
            break
    return highest_id

def search_left(terrain, position):
    return search(terrain, position, step=-1)

def search_right(terrain, position):
    return search(terrain, position, step=1)

def can_step_to(terrain, position, next_position):
    if next_position >= 0 and next_position < len(terrain):
        if terrain[next_position] - terrain[position] == 1:
            return True
    return False




