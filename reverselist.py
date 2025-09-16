
# List to reverse
# l1 = [1, 2, 3, 4, 5]

# # Create an empty list to store reversed result
# l2 = []

# # Go through each item in the list from the end to the start
# for i in range(len(l1) - 1, -1, -1):
#     l2.append(l1[i])

# # Show the result
# print("Original List:", l1)
# print("Reversed List:", l2)

numbers = [1, 2, 3, 4, 5]

# Use slicing [start:stop:step]
reversed_numbers = numbers[::-1]

print("Original List:", numbers)
print("Reversed List:", reversed_numbers)



