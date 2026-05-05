'''

1. Leet code problem:- 283: Move zeroes
2. LeetCode problem:- 268: Missing Number



def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0        
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
        
'''