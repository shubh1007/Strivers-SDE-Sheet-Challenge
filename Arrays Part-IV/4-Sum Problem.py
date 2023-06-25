# CODING NINJAS PROBLEM
from math import *
from collections import *
from sys import *
from os import *

def fourSum(arr, target):
    MAP = {}
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            MAP[arr[i] + arr[j]] = [i, j]
    
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            req_sum = target - (arr[i] + arr[j])
            if req_sum in MAP:
                indices = MAP[req_sum]
                if indices[0] != i and indices[1] != j:
                    return "Yes"
    return "No"

# TIME COMPLEXITY: O(N**2)
# SPACE COMPLEXITY: O(N**2) 






