#sorted check using recursion
from ast import List


def is_SortedArray(nums):
    if len(nums) <= 1:
        return True
    elif nums[0] > nums[1]:
        return False
    else:
        return is_SortedArray(nums[1:])

print(is_SortedArray([10, 20, 30, 40, 50])) #True
print(is_SortedArray([10, 2, 30, 14, 50])) #False

#Leetcode 78. Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        backtrack(0, [])
        return res