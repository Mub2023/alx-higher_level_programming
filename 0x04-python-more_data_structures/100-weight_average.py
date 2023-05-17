#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    Sum_P = 0
    Sum_W = 0
    for x, y in my_list:
        Sum_P += x * y
        Sum_W += y
    return Sum_P / Sum_W
