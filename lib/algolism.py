import copy
import numpy as np

from .position import Position


def in_map(map_size, position: Position) -> bool:
    height, width = map_size
    return 0 <= position.x and position.x < width and\
            0 <= position.y and position.y < height


def pathfinding_algolism1(map_array: np.ndarray):
    map_size = map_array.shape
    count_array = np.full_like(map_array, -1)

    explore_list = []
    goal_point = np.where(map_array == 3)
    goal_point = Position(goal_point[1][0], goal_point[0][0])
    start_point = np.where(map_array == 1)
    start_point = Position(start_point[1][0], start_point[0][0])
    explore_list.append([start_point])
    count_array[start_point.y][start_point.x] = 0

    turn = 0
    done = False
    goal_list = []
    while True:
        turn += 1
        temp_explore_list = []
        for explore in explore_list:
            last_point = explore[-1]
            adjacent_list = last_point.get_adjacent_list()
            for p in adjacent_list:
                if p == goal_point:
                    done = True
                elif not in_map(map_size, p) or map_array[p.y][p.x] == 2:
                    continue
                if count_array[p.y][p.x] != -1 and count_array[p.y][p.x] < turn:
                    continue
                count_array[p.y][p.x] = turn
                append_list = copy.copy(explore)
                append_list.append(p)
                temp_explore_list.append(append_list)
                if p == goal_point:
                    goal_list.append(append_list)
        explore_list = temp_explore_list
        if done or len(explore_list) == 0 or turn > 100:
            break
    return count_array, goal_list
