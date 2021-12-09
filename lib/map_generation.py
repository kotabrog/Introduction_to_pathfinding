import random
import itertools
import numpy as np


def choice_and_del(choice_list, choice_num):
    ret_list = []
    for _ in range(choice_num):
        index = random.choice(range(len(choice_list)))
        ret_list.append(choice_list.pop(index))
    return ret_list


def generation_map(map_size=(6, 6), object_num=0):
    map_array = np.zeros(map_size)
    map_list = list(itertools.product(range(map_size[0]), range(map_size[1])))

    start_coords = choice_and_del(map_list, 1)
    map_array[start_coords[0][0], start_coords[0][1]] = 1

    goal_coords = choice_and_del(map_list, 1)
    map_array[goal_coords[0][0], goal_coords[0][1]] = 3

    if object_num > 0:
        object_coords = choice_and_del(map_list, object_num)
        for object_coord in object_coords:
            map_array[object_coord[0], object_coord[1]] = 2

    return map_array