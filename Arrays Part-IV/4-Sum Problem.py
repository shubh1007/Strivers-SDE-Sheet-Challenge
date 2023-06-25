# CODING NINJAS SOLUTION
from typing import List
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


# LEETCODE SOLUTION
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # req_sum = target - (nums[i] + nums[j])
                left = j + 1
                right = n - 1
                while left < right:
                    # curr_sum = nums[left] + nums[right]
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res






