# Module 3: Data Structures Assignments
## Lesson 3.2: Tuples
### Assignment 1: Creating and Accessing Tuples
# Create a tuple with the first 10 positive integers. Print the tuple.

# h = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for i in h:
#     if i >0:
#         print(i)

# ### Assignment 2: Accessing Tuple Elements
# Print the first, middle, and last elements of the tuple created in Assignment 1.

# print(h[0])
# print(h[len(h)//2])
# print(h[-1])

# ### Assignment 3: Tuple Slicing
# Print the first three elements, the last three elements, 
# and the elements from index 2 to 5 of the tuple created in Assignment 1.

# print(h[:3])  # First three elements
# print(h[-3:])  # Last three elements
# print(h[2:6])  # Elements from index 2 to 5

# ### Assignment 4: Nested Tuples
# Create a nested tuple representing a 3x3 matrix and print the matrix.
#  Access and print the element at the second row and third column.

# Creating a nested tuple (3x3 matrix)

# matrix = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9)
# )

# # Print the entire matrix
# print("Matrix:")
# for row in matrix:
#     print(row)

# # Access and print the element at second row and third column
# print("\nElement at second row and third column:")
# print(matrix[1][2])

# ### Assignment 5: Tuple Concatenation
# Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple

# t= (1, 2, 3) + (4, 5, 6)
# print(t)


# ### Assignment 6: Tuple Methods
# Create a tuple with duplicate elements and count the occurrences of an element.
#  Find the index of the first occurrence of an element in the tuple.


# Create a tuple with duplicate elements

# numbers = (10, 20, 30, 20, 40, 20, 50)
# count_20 = numbers.count(20)
# index_20 = numbers.index(20)

# print("Tuple:", numbers)
# print("Count of 20:", count_20)
# print("First index of 20:", index_20)


# ### Assignment 7: Unpacking Tuples
# Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.


# Create a tuple with 5 elements

# data = (10, 20, 30, 40, 50)
# # Unpack the tuple into 5 variables
# a, b, c, d, e = data
# # Print the variables
# print("a =", a)
# print("b =", b)
# print("c =", c)
# print("d =", d)
# print("e =", e)

# ### Assignment 8: Tuple Conversion
# Convert a list of the first 5 positive integers to a tuple. Print the tuple.

# lst = [1, 2, 3, 4, 5]
# p = tuple(lst)
# print(p)

# ### Assignment 9: Tuple of Tuples
# Create a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.

# tuple_of_tuples = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9)
# )

# for t in tuple_of_tuples:
#     print(t)

# for i in tuple_of_tuples:
#     print(i)

# ### Assignment 10: Tuple and List
# Create a tuple with the first 5 positive integers. 
# Convert it to a list, append the number 6, and convert it back to a tuple.
#  Print the resulting tuple.

# n = (1, 2, 3, 4, 5)
# j = list(n)
# j.append(6)
# u = tuple(j)
# print(u)

# ### Assignment 11: Tuple and String
# Create a tuple with the characters of a string.
# Join the tuple elements into a single string. 
# Print the string.


# text = "Python"
# char_tuple = tuple(text)
# new_string = "".join(char_tuple)
# print("Tuple:", char_tuple)
# print("String:", new_string)

# ### Assignment 12: Tuple and Dictionary
# Create a dictionary with tuple keys and integer values. Print the dictionary.

# my_dict = {
#     (1, 2): 10,
#     (3, 4): 20,
#     (5, 6): 30
# }

# for key, value in my_dict.items():
#     print("Key:", key, "Value:", value)

# ### Assignment 13: Nested Tuple Iteration
# Create a nested tuple and iterate over the elements, printing each element.

# nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# for inner_tuple in nested_tuple:
#     for element in inner_tuple:
#         print(element)

# ### Assignment 14: Tuple and Set
# Create a tuple with duplicate elements. 
# Convert it to a set to remove duplicates and print the resulting set.

duplicate_tuple = (1, 2, 3, 2, 4, 1, 5)
unique_set = set(duplicate_tuple)
print("Tuple with duplicates:", duplicate_tuple)
print("Set without duplicates:", unique_set)

# ### Assignment 15: Tuple Functions
# Write functions that take a tuple and return the minimum, maximum, and sum of the elements.
#  Print the results for a sample tuple.

# def tuple_min(t):
#     return min(t)       
# def tuple_max(t):
#     return max(t)
# def tuple_sum(t):
#     return sum(t)   
# sample_tuple = (10, 20, 30, 40, 50)
# print("Sample Tuple:", sample_tuple)
# print("Minimum:", tuple_min(sample_tuple))
# print("Maximum:", tuple_max(sample_tuple))
# print("Sum:", tuple_sum(sample_tuple))