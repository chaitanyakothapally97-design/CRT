#Plus One Problem
import array as array
arr = array.array('i', [1, 2, 3])
for i in range(arr):
    arr = arr % 10
print(arr)