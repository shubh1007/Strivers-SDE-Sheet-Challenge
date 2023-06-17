class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        count = {}
        for i in range(1, len(A) + 1):
            count[i] = 0
        for i in A:
            count[i] += 1
        a, b = -1, -1
        for key, val in count.items():
            if val == 0:
                b = key
            if val == 2:
                a = key
        return [a, b]
    
# Approach:
# Step 1: Create a dictionary with keys as 1 to n and values as 0.
# Step 2: Traverse the array and increment the value of the key by 1.
# Step 3: Traverse the dictionary and find the key with value 0 and 2.
# Step 4: Return the key with value 0 and 2.
#
# Time Complexity: O(n)
# Space Complexity: O(n)