'''
Arrays - Advanced

1) Two Sum-> 1
2) Maximum Subarray -> 53
3)Majority Element -> 169
'''
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         a = nums[0]
#         b = nums[0]        
#         for i in range(1, len(nums)):
#             a = max(nums[i], a + nums[i])
#             b = max(a, b)
#         return b

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate = None
#         count = 0
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             if num == candidate:
#                 count += 1
#             else:
#                 count -= 1
#         return candidate