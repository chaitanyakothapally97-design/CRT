'''
1. Find the largest number in a list of integers.
2. check palindrome using reversed() function and join() method.
3. count even numbers using filter() function
4. Remove duplicates from a list using set() function
5. Sum of digits using sum() function
6. sort words alphabetically using sorted() function
7. Find common elements using set
8. Index with value using enumerate() function
9. Pair two lists using zip() function
10. Find second largest number using sorted() function
'''
#1. 
# arr = [10, 20, 5, 15, 30]
# largest = max(arr)
# print("The largest number is:", largest)

#2. check palindrome using reversed() function and join() method.
# str1 = "madam"
# str2 = ''.join(reversed(str1))
# if str1 == str2:
#     print("Palindrome.")
# else:
#     print("Not a palindrome.")

#3. count even numbers using filter() function
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, arr))
# print(even_numbers)

#4. Remove duplicates from a list using set() function
# arr = [1, 2, 3, 4, 5, 2, 3, 6]
# unique_numbers = list(set(arr)) 
# print(unique_numbers)

#5. Sum of digits using sum() function
# num = 12345
# digit_sum = sum(int(digit) for digit in str(num))   
# print(digit_sum)

#6. sort words alphabetically using sorted() function
# words = ["banana", "apple", "cherry", "date"]
# sorted_words = sorted(words)    
# print(sorted_words)

#7. Find common elements using set
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [4, 5, 6, 7, 8]
# common_elements = list(set(arr1) & set(arr2))
# print(common_elements)

#8. Index with value using enumerate() function
# arr = ['a', 'b', 'c', 'd']
# for index, value in enumerate(arr):
#     print(f"Index: {index}, Value: {value}")

#9. Pair two lists using zip() function
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# paired = list(zip(list1, list2))
# print(paired)

#10. Find second largest number using sorted() function
arr = [10, 20, 5, 15, 30]
sorted_arr = sorted(arr, reverse=True)
second_largest = sorted_arr[1]
print(second_largest)