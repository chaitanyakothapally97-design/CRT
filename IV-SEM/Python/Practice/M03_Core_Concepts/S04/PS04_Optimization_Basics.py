a = [3, 1, 4, 1, 5, 9]
for num in a:
    print(num + num)

#2. Maximum element in a list
def max_element(lst: list) -> int:
    if not lst:
        return None 
    max_value = lst[0]  
    for num in lst:
        if num > max_value:
            max_value = num  
    return max_value