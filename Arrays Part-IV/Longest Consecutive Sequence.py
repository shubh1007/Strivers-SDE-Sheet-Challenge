from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_streak = 0
        
        for num in nums:
            if num - 1 not in hashset:
                curr_streak = 1
                curr_num = num
                while curr_num + 1 in hashset:
                    curr_num += 1
                    curr_streak += 1
                max_streak = max(max_streak, curr_streak)
        return max_streak
