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

def find_best_action_2(park, char_on_left=True):
    if not char_on_left:
        park = park[::-1]   # reverse park

    v_max = park[0] 
    sum = 0
    for v in park:
        sum += v
        if v_max < sum:
            v_max = sum

    return v_max

def get_next_move(parks, char_on_left=True):
    
    move_to_predict = min(3, len(parks))
    act_1 = get_next_reward(parks, 1, move_to_predict, char_on_left) 
    act_2 = get_next_reward(parks, 2, move_to_predict, char_on_left)
    act_3 = get_next_reward(parks, 3, move_to_predict, char_on_left)

    best_act = 1 + np.argmax([act_1, act_2, act_3]) 

    # print(find_best_action_2(parks[0], char_on_left))
    
    if best_act == 1:
        reward = 0
    elif best_act == 2:
        reward = find_best_action_2(parks[0], char_on_left)
    else:
        reward = sum(parks[0])

    return best_act, reward

def get_next_reward(parks, action, move_to_predict, char_on_left=True):
    if move_to_predict == 0 or len(parks)<move_to_predict:
        return 0

    if action==3:
        char_on_left = not char_on_left

    max_reward = max([get_next_reward(parks[1:], 1, move_to_predict-1, char_on_left),
                 get_next_reward(parks[1:], 2, move_to_predict-1, char_on_left),
                 get_next_reward(parks[1:], 3, move_to_predict-1, char_on_left)])

    if action==1:
        return max_reward + 0
    if action==2:
        return max_reward + find_best_action_2(parks[0], char_on_left)
    if action==3:
        return max_reward + sum(parks[0])

@timing
def solve(parks):
    char_on_left = True
    rewards = 0
    for i in range(len(parks)):
        act, reward = get_next_move(parks[i:], char_on_left)
        print('{}: {}'.format(act, reward))
        rewards += reward
        if act == 3:
            char_on_left = not char_on_left
    return rewards


parks = [[1,4,-5],
        [-1,-9,100]]

parks = [[1,4,-5],
[-1,-1,100]]

parks = [[-9,-8,1,2,3]]

def create_random_case(n, m):
    case = []
    for i in range(n):
        case.append([randint(-100, 100) for j in range(m)])
    return case
            

case = create_random_case(4, 5)
# case = []
# with open('testcase', 'r') as f:
#     for line in f.readlines():
#         nums = line.split(' ')
#         case.append([int(num) for num in nums])

result = solve(case)
for r in case:
    print(r)
print('ANSWER')
print(result)


