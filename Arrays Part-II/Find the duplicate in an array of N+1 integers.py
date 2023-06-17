from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# Approach: Floyd's Tortoise and Hare (Cycle Detection)
# Step 1: Initialize two pointers slow and fast to the first index.
# Step 2: Move slow by one step and fast by two steps.
# Step 3: If slow and fast meet then there is a cycle.
# Step 4: Move fast to the first index.
# Step 5: Move slow and fast by one step.
# Step 6: If slow and fast meet then return slow.
# Step 7: Else return -1.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

