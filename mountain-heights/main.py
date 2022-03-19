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

def find_peaks(terrain, ground_ids):
    peak_ids = []
    for ground_id in ground_ids:
        left_peak = search_left(terrain, ground_id)
        right_peak = search_right(terrain, ground_id)
        if left_peak:
            peak_ids.append(left_peak)
        if right_peak:
            peak_ids.append(right_peak)

    peak_values = [terrain[peak_id] for peak_id in peak_ids]
    return peak_ids, peak_values

def find_highest_peak(terrain):
    ground_ids = find_all_grounds(terrain)
    peak_ids, peak_values = find_peaks(terrain, ground_ids)
    if peak_ids:
        highest_peak = max(peak_values)
        highest_peak_id = peak_ids[peak_values.index(highest_peak)]
        return highest_peak_id, highest_peak
    return -1, -1


def main():
    # terrain = [1, 2, 3, 2, 3, 4, 2, 3, 2, 5]
    # terrain = [3, 2, 3, 2, 3, 4, 3, 2, 1, 4]
    terrain = [3, 2, 3, 2, 3, 4, 3, 2, 5, 4]
    result  = find_highest_peak(terrain)
    print(result)

main()
