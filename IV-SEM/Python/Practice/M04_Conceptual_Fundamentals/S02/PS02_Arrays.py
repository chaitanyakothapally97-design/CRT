'''
1. Reverse the array elements.
     a. Using Slicing
     b. Using reverse() 
     c. Using For Loop
2. Chech if an array is sorted.
3. Find Max and Min Elements
4. Find Second Largest Element
5. Find duplicates from Array
6. Count frequency of Elements
7. Rotate Array

# a. Using Slicing
arr = list(map(int, input("Enter an Array: ").split()))
reversed_arr = arr[::-1]
print("Reversed array using slicing:", reversed_arr)

# b. Using reverse()
arr = list(map(int, input("Enter an Array: ").split()))
arr.reverse()
print("Reversed array using reverse():", arr)

# c. Using For Loop
arr = list(map(int, input("Enter an Array: ").split()))
reversed_arr = []
for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])
print("Reversed array using for loop:", reversed_arr)


#2. Chech if an array is sorted.
arr = list(map(int, input("Enter an Array: ").split()))
b = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        b = False
print(b)

#3 Find Max and Min Elements
arr = list(map(int, input("Enter an Array: ").split()))
max_element = arr[0]
min_element = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
    if arr[i] < min_element:
        min_element = arr[i]
print("Maximum element:", max_element)
print("Minimum element:", min_element)

#4 Find Second Largest Element
arr = list(map(int, input("Enter an Array: ").split()))
max_element = arr[0]
second_largest = float('-inf')
for i in range(1, len(arr)):
    if arr[i] > max_element:
        second_largest = max_element
        max_element = arr[i]
    elif arr[i] > second_largest and arr[i] != max_element:
        second_largest = arr[i]
if second_largest == float('-inf'):
    print("No second largest element found.")
else:
    print("Second largest element:", second_largest)

#5 Find duplicates from Array
arr = list(map(int, input("Enter an Array: ").split()))
duplicates = set()
seen = set()
for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
if duplicates:
     print("Duplicate elements:", duplicates)
else:
     print("No duplicate elements found.")

#6 Count frequency of Elements
arr = list(map(int, input("Enter an Array: ").split()))
frequency = {}
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("Frequency of elements:")
for num, count in frequency.items():
     print(f"{num}: {count}")
'''
#7 Rotate array
from ast import List


arr = list(map(int, input("Enter an Array: ").split()))
n = len(arr)
k = int(input("Enter number of positions to rotate: "))
k = k % n  # Handle cases where k is greater than n
rotated_arr = arr[-k:] + arr[:-k]
print("Rotated array:", rotated_arr)

# LeetCode Problem 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == (total_sum - left_sum - nums[i]):
                return i
            left_sum += nums[i]
        return -1