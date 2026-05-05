#Implement Lower Bound
def Binary_Search(nums, target):
    nums.sort()
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

print(Binary_Search([2, 3, 7, 10, 11, 11, 25], 50))

