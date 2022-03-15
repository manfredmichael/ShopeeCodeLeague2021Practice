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
        self.x = int(x)
        self.y = int(y)
        self.signal = 0

    def is_inside(self, hub, r):
        return (self.x - hub.x)**2 + (self.y - hub.y)**2 <= r**2 

    def add_signal(self, hub, r):
        if self.is_inside(hub, r):
            self.signal += 1
    
    def reset(self):
        self.signal = 0

class Hub:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SignalChecker:
    @staticmethod
    def get_nosignal_engineers(engineers):
        return len([e for e in engineers if e.signal != 1])

def get_input(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    n_engineer = int(lines[0])
    n_query = int(lines[n_engineer+2])
    coor_engineers = [(int(line.split(' ')[0]), int(line.split(' ')[1])) for line in lines[1:1+n_engineer]]
    range_query = [(int(line.split(' ')[0]), int(line.split(' ')[1]))for line in lines[n_engineer+3:n_engineer+3+n_query]]
    coor_hubs = [int(coor) for coor in lines[n_engineer+1].split(' ')]
    return coor_hubs, coor_engineers, range_query

def main():
    coor_hubs, coor_engineers, range_query = get_input('testcase')
    Cg = Hub(coor_hubs[0], coor_hubs[1])
    Ca = Hub(coor_hubs[2], coor_hubs[3])
    engineers = [Engineer(x, y) for x, y in coor_engineers]
    for Rg, Ra in range_query:
        for engineer in engineers:
            engineer.add_signal(Cg, Rg)
            engineer.add_signal(Ca, Ra)
        result = SignalChecker.get_nosignal_engineers(engineers)
        print(result)
        for engineer in engineers:
            engineer.reset()


if __name__=='__main__':
    main()
