from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if res and res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
        return res
    