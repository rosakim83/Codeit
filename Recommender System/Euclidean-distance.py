import numpy as np
from math import sqrt


def distance(user_1, user_2):
    diff = (user_1 - user_2) ** 2
    return sqrt(np.sum(diff))


user_1 = np.array([0, 1, 2, 3, 4, 5])
user_2 = np.array([0, 1, 4, 6, 1, 4])

print(distance(user_1, user_2))
