'''
#Merge sort
def Merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def Merge_Sort(nums):
    left = []
    right = []
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = Merge_Sort(nums[:mid])
    right = Merge_Sort(nums[mid:])
    return Merge(left, right)

print(Merge_Sort([14, 7, 3, 12])) #[3, 7, 12, 14]
'''

#Quick sort
#Identify pivot element index
def Partition(nums, low, high):
    pivot = nums[low]
    i = low  + 1
    j = high
    while True:
        while i <= j and nums[i] <= pivot:
            i += 1
        while i <= j and nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break
    nums[low], nums[j] = nums[j], nums[low]
    return j

def Quick_Sort(nums, low, high):
    if low < high:
        pi = Partition(nums, low, high)
        Quick_Sort(nums, low, pi - 1)
        Quick_Sort(nums, pi + 1, high)
    return nums

print(Quick_Sort([14, 7, 3, 12], 0, 3)) #[3, 7, 12, 14]