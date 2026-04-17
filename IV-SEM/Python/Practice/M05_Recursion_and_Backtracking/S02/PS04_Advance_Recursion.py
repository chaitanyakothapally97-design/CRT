#Digital Root using Recursion
def Digital_Root(n):
    if n < 10:
        return n
    else:
        s = sum([int(i) for i in str(n)])
        return Digital_Root(s)
print(Digital_Root(16)) #7
print(Digital_Root(96)) #6

#Check if Array is Sorted using Recursion
def Sorted_Array(nums, i):
    if i == len(nums) - 1:
        return True
    elif nums[i] > nums[i+1]:
        return False
    else:
        return Sorted_Array(nums, i+1)
print(Sorted_Array([1, 2, 3, 4, 5], 0)) #True
print(Sorted_Array([1, 2, 3, 5, 4], 0)) #False

