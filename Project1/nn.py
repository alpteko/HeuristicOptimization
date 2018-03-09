import numpy as np


def dist(c1, c2):
    return np.linalg.norm(c1-c2)


def calculate_tour(tour):
    t = len(tour)
    l = 0
    for i in range(t-1):
        l += dist(tour[i], tour[i+1])
    return l


def find_min(city, city_map):
    minimum = 100
    target = 0
    for i, c in enumerate(city_map):
        if minimum > dist(city, c):
            target = i
            minimum = dist(city, c)
    return target, minimum


def one_sided_nn(index, city_map):
    city = city_map[index]
    city_map.pop(index)
    tour = [city]
    while len(city_map) > 0:
        index,_ = find_min(city, city_map)
        city = city_map[index]
        tour.append(city)
        city_map.pop(index)
    tour.append(tour[0])
    return tour


def two_sided_nn(index, city_map):
    city1 = city_map[index]
    city2 = city_map[index]
    city_map.pop(index)
    tour = [city1]
    while len(city_map) > 0:
        index1, cost1 = find_min(city1, city_map)
        index2, cost2 = find_min(city2, city_map)
        if cost1 < cost2:
            tour.insert(0, city_map[index1])
            city_map.pop(index1)
        else:
            tour.append(city_map[index2])
            city_map.pop(index2)
        city1 = tour[0]
        city2 = tour[-1]
    tour.append(tour[0])
    return tour



