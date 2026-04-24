'''
1. Linear search(sequential search)
    Best Case ==> O(1)
    Worst Case ==> O(n)
    Average Case ==> O(n)
2. Binary search(Interval search)
    Best Case ==> O(1)
    Worst Case ==> O(log n)
    Average Case ==> O(log n)
'''

def Linear_Search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

print(Linear_Search([12, 25, 36, 47, 58], 36)) #2


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

    return -1

print(Binary_Search([12, 25, 36, 47, 10, 58], 10))