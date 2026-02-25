def linear_search(elements, target):
    for i in range(len(elements)):
        if target == elements[i]:
            return i
    return -1

print(linear_search([1, 2, 3, 4, 5, 6], 6))
print(linear_search([97, 96, 98, 95], 96))
print(linear_search([1, 2, 4, 3, 5, 6], 1))