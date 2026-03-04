''' 
Set:
1. Use {} to create a set.
2. Set does not allow duplicate values.
3. Set is unindexed.
4. Set is mutable.
5. Set is unordered.
6. Set is heterogeneous.

#Adding elements to a set
A = {1, 2, 3}
B = {3, 4, 5}
A.add(4)
B.update({6, 7})
print(A, B)

#Removing elements from a set
A.pop()
print(A)
print(help(set))

#LeetCode problem: 268. Given an array nums containing n distinct numbers in the range [0, n], return 
# the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

#LeetCode Problem.349: Given two integer arrays nums1 and nums2, return an array of their intersection.
#Each element in the result must be unique and you may return the result in any order.
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
'''

#S02. Tuples:
'''
Tuples:
1. Definition: It is an ordered and immutable collection of data. 
    Symbol: it is represented by parentheses "()".
2. Immmutable
3. Accessing -> index positions +ve or -ve
4. Concatenation -> 
5. Repetition of tuples -> Repeating a tuple multiple times
6. Nesting of tuples -> Tuple inside a tuple
7. Slicing of tuples -> Extracting a portion of a tuple using slicing syntax
8. Deleting a tuple -> 
9. LeetCode problems on tuples (349, 657)

t = (10, 23, 96, 45, 67)
t1 = ("Chaitu", "Sindhu", "Aadhya")
#t[0] = 50
print(t[0])
print(t[-1])
print(t + t1)
print(t, t1)
print(t * 3)
print(t[1:4])
print(t[:5])
print(t[:-1])
del t
print(t)

#LeetCode problem: 349. Given two integer arrays nums1 and nums2, return an array of their intersection.
#Each element in the result must be unique and you may return the result in any order.
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
    
#LeetCode problem: 657. There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves,
#  judge if this robot ends up at (0, 0) after it completes its moves.
class Solution:
    def judgeCircle(self, moves):
        x = 0
        y = 0
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        return x == 0 and y == 0
'''
#S03. Dictionaries:
'''
1. Definition: Stores Data in form of key and value pairs. 
2.Create a dictionary using {} and key-value pairs separated by a colon (:).
3. Accessing values in a dictionary using keys.
'''
d = {"name": "Chaitu", "age": 21}
print(d)
d2 = dict(name="Chinnu", age=18)
print(d2)
print(d2["name"])
print(d2.get("age"))
print(d2.keys())
print(d2.values())
d2['Place'] = 'Hyderabad'
print(d2)
del d2['age']
print(d2)

'''
LeetCode problem: 1. Two Sum: Given an array of integers nums and an integer target,
 return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
'''