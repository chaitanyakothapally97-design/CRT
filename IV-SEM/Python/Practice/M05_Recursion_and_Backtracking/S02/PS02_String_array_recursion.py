'''
#Calculate the sum of all elements in a list
def Array_Sum(nums):
    s = 0
    stop = -1 * (len(nums) + 1)
    for i in range(-1, stop, -1):
        s += nums[i]
    return s

print(Array_Sum([10, 20, 30, 40]))#100

#Calculate the sum of all elements in a list using Recursion
def Array_Sum(nums):
    if len(nums) == 0:
        return 0
    else:
      return nums[-1] + Array_Sum(nums[:-1])

print(Array_Sum([10, 20, 30, 40]))#100

#Reverse a list
def Reverse_Array(nums):
    r = []
    for i in range(-1, -1 * (len(nums) + 1), -1):
        r.append(nums[i])
    return r
    
print(Reverse_Array([10, 20, 30, 40]))#[40, 30, 20, 10]

#Reverse a list with inplace method
def Reverse_Array(nums, i, j):
    if i >= j:
        return 
    nums[i], nums[j] = nums[j], nums[i]
    Reverse_Array(nums, i+1, j-1)
    return nums
print(Reverse_Array([10, 20, 30, 40], 0, 3))#[40, 30, 20, 10]

#Reverse a String
def Reverse_str(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + Reverse_str(s[:-1])

print(Reverse_str("python")) #nohtyp
'''
#Check if a String is Palindrome or not
def Palindrome(s):
    def Reverse_str(s):
        if len(s) == 0:
            return ""
        else:
            return s[-1] + Reverse_str(s[:-1])
    if s == Reverse_str(s):
        return True
    else:     
        return False
print(Palindrome("python")) #False
print(Palindrome("madam")) #True