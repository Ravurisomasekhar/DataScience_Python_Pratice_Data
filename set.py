# # Module 3: Data Structures Assignments
# ## Lesson 3.3: Sets
# ### Assignment 1: Creating and Accessing Sets
# Create a set with the first 10 positive integers. Print the set.

# set_of_integers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(set_of_integers)

# ### Assignment 2: Adding and Removing Elements
# Add the number 11 to the set created in Assignment 1. 
# Then remove the number 1 from the set. Print the modified set.

# set_of_integers.remove(1)
# print(set_of_integers)

# ### Assignment 3: Set Operations
# Create two sets: one with the first 5 positive integers and another with 
# the first 5 even integers. Perform and print the results of union, intersection, 
# difference, and symmetric difference operations on these sets.

# # First 5 positive integers
# set1 = {1, 2, 3, 4, 5}
# # First 5 even integers
# set2 = {2, 4, 6, 8, 10}
# # Union
# print("Union:", set1.union(set2))
# # Intersection
# print("Intersection:", set1.intersection(set2))

# # Difference (set1 - set2)
# print("Difference (set1 - set2):", set1.difference(set2))

# # Difference (set2 - set1)
# print("Difference (set2 - set1):", set2.difference(set1))

# # Symmetric Difference
# print("Symmetric Difference:", set1.symmetric_difference(set2))

# ### Assignment 4: Set Comprehensions
# Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.

# # Create a set of squares of the first 10 positive integers
# squares = {num ** 2 for num in range(1, 11)}

# # Print the set
# print("Squares Set:", squares)

# ### Assignment 5: Filtering Sets
# Create a new set containing only the even numbers from the set 
# created in Assignment 1 using a set comprehension. Print the new set.

# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# even_numbers = {num for num in numbers if num % 2 == 0}

# print(even_numbers)




# ### Assignment 6: Set Methods
# Create a set with duplicate elements and remove the duplicates using set methods. Print the modified set.

# numbers = [1, 2, 2, 3, 4, 4, 5]

# unique_numbers = set(numbers)

# print(unique_numbers)


# ### Assignment 7: Subsets and Supersets
# Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}

# print("Subset:", set2.issubset(set1))
# print("Superset:", set1.issuperset(set2))



# ### Assignment 8: Frozenset
# Create a frozenset with the first 5 positive integers. Print the frozenset.


# frozen_set = frozenset({1, 2, 3, 4, 5})

# print(frozen_set)


# ### Assignment 9: Set and List Conversion
# Create a set with the first 5 positive integers. Convert it to a list, 
# append the number 6, and convert it back to a set. Print the resulting set.


# numbers = {1, 2, 3, 4, 5}

# numbers_list = list(numbers)
# numbers_list.append(6)

# numbers = set(numbers_list)

# print(numbers)

# ### Assignment 10: Set and Dictionary
# Create a dictionary with set keys and integer values. Print the dictionary.


# my_dict = {
#     frozenset({1, 2}): 10,
#     frozenset({3, 4}): 20
# }

# print(my_dict)



# ### Assignment 11: Iterating Over Sets
# Create a set and iterate over the elements, printing each element.


# numbers = {1, 2, 3, 4, 5}

# for num in numbers:
#     print(num)


# ### Assignment 12: Removing Elements from Sets
# Create a set and remove elements from it until it is empty. Print the set after each removal.

# numbers = {1, 2, 3, 4, 5}

# while numbers:
#     removed = numbers.pop()
#     print("Removed:", removed)
#     print("Current Set:", numbers)

# ### Assignment 13: Set Symmetric Difference Update
# Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.


# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# set1.symmetric_difference_update(set2)

# print(set1)


# ### Assignment 14: Set Membership Testing
# Create a set and test if certain elements are present in the set. Print the results.



# numbers = {1, 2, 3, 4, 5}

# print(3 in numbers)
# print(7 in numbers)




# ### Assignment 15: Set of Tuples
# Create a set containing tuples, where each tuple contains two elements. Print the set.

# tuple_set = {
#     (1, 2),
#     (3, 4),
#     (5, 6)
# }

# print(tuple_set)