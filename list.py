# # Module 3: Data Structures Assignments
# ## Lesson 3.1: Lists
# ### Assignment 1: Creating and Accessing Lists

# Cr
# eate a list of the first 20 positive integers. Print the list.

# n = list(range(1, 21))
# print(n)


# ### Assignment 2: Accessing List Elements
# Print the first, middle, and last elements of the list created in Assignment 1.


# print(n[0])  # First element
# print(n[len(n) // 2])  # Middle element
# print(n[-1])  # Last element



# ### Assignment 3: List Slicing
# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.

# print(n[:5])  # First five elements
# print(n[-5:])  # Last five elements
# print(n[5:16])  # Elements from index 5 to 15

# ### Assignment 4: List Comprehensions
# Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.

# number = [i**2 for i in range(1, 11)]
# print(number)

# ### Assignment 5: Filtering Lists
# Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.

# number = [i for i in n if i % 2 == 0]
# print(number)

# ### Assignment 6: List Methods
# Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.


# import random

# random_numbers = [random.randint(1, 100) for _ in range(20)]
# print(random_numbers)

# accending_order = sorted(random_numbers)
# print(accending_order)

# descending_order = sorted(random_numbers, reverse=True)
# print(descending_order)

# ### Assignment 7: Nested Lists
# Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.

# n= [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]  
# print(n)
# print(n[1][2])  # Accessing the element at the second row and third column

# ### Assignment 8: List of Dictionaries
# Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. 
# Sort the list of dictionaries by the 'score' in descending order and print the sorted list.

# 
# dict = [{'name': 'Alice', 'score': 85},
#         {'name': 'Bob', 'score': 92},
#         {'name': 'Charlie', 'score': 78}]   
# print(sorted(dict, key=lambda x: x['score'], reverse=True))

# ### Assignment 9: Matrix Transposition
# Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose.
# Print the original and transposed matrices.

# def transpose_matrix(matrix):
#     transposed = []

#     for col in range(3):
#         row = []
#         for r in range(3):
#             row.append(matrix[r][col])
#         transposed.append(row)

#     return transposed


# # Input matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Find transpose
# transposed = transpose_matrix(matrix)

# # Print original matrix
# print("Original Matrix:")
# for row in matrix:
#     print(row)

# # Print transposed matrix
# print("\nTransposed Matrix:")
# for row in transposed:
#     print(row)

# ### Assignment 10: Flattening a Nested List
# Write a function that takes a nested list and flattens it into a single list. 
# Print the original and flattened lists.

# def flatten_list(nested_list):
#     flattened = []

#     for sublist in nested_list:
#         for item in sublist:
#             flattened.append(item)

#     return flattened


# # Original nested list
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# # Flatten the list
# flattened = flatten_list(nested_list)

# # Print results
# print("Original Nested List:")
# print(nested_list)

# print("\nFlattened List:")
# print(flattened)

# ### Assignment 11: List Manipulation
# Create a list of the first 10 positive integers. 
# Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. 
# Print the modified list.


# # Create a list of the first 10 positive integers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original List:")
# print(numbers)
# # Remove elements at indices 6, 4, and 2
# # (Remove in reverse order to avoid index shifting)
# numbers.pop(6)
# numbers.pop(4)
# numbers.pop(2)

# # Insert 99 at index 5
# numbers.insert(5, 99)

# # Print the modified list
# print("Modified List:")
# print(numbers)

# ### Assignment 12: List Zipping
# Create two lists of the same length. 
# Use the `zip` function to combine these lists into a list of tuples and print the result.

# Create two lists of the same length
names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 22, 28]

# Zip the lists together
combined = list(zip(names, ages))

# Print the result
print("Combined List of Tuples:")
print(combined)

# ### Assignment 13: List Reversal
# Write a function that takes a list and returns a new list with the elements in reverse order. 
# Print the original and reversed lists.

# def reverse_list(lst):
#     reversed_lst = []

#     for i in range(len(lst) - 1, -1, -1):
#         reversed_lst.append(lst[i])

#     return reversed_lst


# # Original list
# numbers = [10, 20, 30, 40, 50]

# # Reverse the list
# reversed_numbers = reverse_list(numbers)

# # Print results
# print("Original List:")
# print(numbers)

# print("\nReversed List:")
# print(reversed_numbers)

# ### Assignment 14: List Rotation
# Write a function that rotates a list by n positions. Print the original and rotated lisst.

# def rotate_list(lst, n):
#     n = n % len(lst)  # Handle rotations larger than list length
#     return lst[n:] + lst[:n]


# # Original list
# numbers = [1, 2, 3, 4, 5, 6]

# # Rotate by 2 positions
# rotated = rotate_list(numbers, 2)

# # Print results
# print("Original List:")
# print(numbers)

# print("\nRotated List:")
# print(rotated)


# ### Assignment 15: List Intersection
# Write a function that takes two lists and returns a new list containing only the elements 
# that are present in both lists. Print the intersected list.

# def intersection(list1, list2):
#     result = []

#     for item in list1:
#         if item in list2 and item not in result:
#             result.append(item)

#     return result


# # Example lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# # Find intersection
# common_elements = intersection(list1, list2)

# # Print result
# print("List 1:", list1)
# print("List 2:", list2)
# print("Intersected List:", common_elements)
