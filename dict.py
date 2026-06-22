# Module 3: Data Structures Assignments
## Lesson 3.4: Dictionaries

### Assignment 1: Creating and Accessing Dictionaries
# Create a dictionary with the first 10 positive integers as keys and their squares as values.
#  Print the dictionary.



# ### Assignment 2: Accessing Dictionary Elements
# Print the value of the key 5 and the keys of the dictionary created in Assignment 1.

# ### Assignment 3: Dictionary Methods
# Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.

# ### Assignment 4: Iterating Over Dictionaries
# Iterate over the dictionary created in Assignment 1 and print each key-value pair.

# ### Assignment 5: Dictionary Comprehensions
# Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.

# ### Assignment 6: Merging Dictionaries
# Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.

# ### Assignment 7: Nested Dictionaries
# Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.

# ### Assignment 8: Dictionary of Lists
# Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.

# ### Assignment 9: Dictionary of Tuples
# Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.

# ### Assignment 10: Dictionary and List Conversion
# Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.

# ### Assignment 11: Dictionary Filtering
# Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.

# ### Assignment 12: Dictionary Key and Value Transformation
# Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary.

# ### Assignment 13: Default Dictionary
# Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.

# ### Assignment 14: Counting with Dictionaries
# Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.

# ### Assignment 15: Dictionary and JSON
# Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.



# ANSWER:

# ==========================
# Assignment 1: Creating and Accessing Dictionaries
# ==========================
squares = {i: i**2 for i in range(1, 11)}
print("Assignment 1:", squares)

# ==========================
# Assignment 2: Accessing Dictionary Elements
# ==========================
print("\nAssignment 2:")
print("Value of key 5:", squares[5])
print("Keys:", list(squares.keys()))

# ==========================
# Assignment 3: Dictionary Methods
# ==========================
squares[11] = 121
del squares[1]
print("\nAssignment 3:", squares)

# ==========================
# Assignment 4: Iterating Over Dictionaries
# ==========================
print("\nAssignment 4:")
for key, value in squares.items():
    print(key, ":", value)

# ==========================
# Assignment 5: Dictionary Comprehensions
# ==========================
cubes = {i: i**3 for i in range(1, 11)}
print("\nAssignment 5:", cubes)

# ==========================
# Assignment 6: Merging Dictionaries
# ==========================
dict1 = {i: i**2 for i in range(1, 6)}
dict2 = {i: i**2 for i in range(6, 11)}
merged_dict = {**dict1, **dict2}
print("\nAssignment 6:", merged_dict)

# ==========================
# Assignment 7: Nested Dictionaries
# ==========================
student = {
    "name": "Somasekhar",
    "age": 22,
    "grades": {
        "math": 90,
        "science": 85,
        "english": 88
    }
}
print("\nAssignment 7:", student)

# ==========================
# Assignment 8: Dictionary of Lists
# ==========================
multiples = {i: [i*j for j in range(1, 6)] for i in range(1, 6)}
print("\nAssignment 8:", multiples)

# ==========================
# Assignment 9: Dictionary of Tuples
# ==========================
tuple_dict = {i: (i, i**2) for i in range(1, 6)}
print("\nAssignment 9:", tuple_dict)

# ==========================
# Assignment 10: Dictionary and List Conversion
# ==========================
square_dict = {i: i**2 for i in range(1, 6)}
tuple_list = list(square_dict.items())
print("\nAssignment 10:", tuple_list)

# ==========================
# Assignment 11: Dictionary Filtering
# ==========================
square_dict = {i: i**2 for i in range(1, 11)}
even_dict = {k: v for k, v in square_dict.items() if k % 2 == 0}
print("\nAssignment 11:", even_dict)

# ==========================
# Assignment 12: Dictionary Key and Value Transformation
# ==========================
square_dict = {i: i**2 for i in range(1, 6)}
swapped_dict = {v: k for k, v in square_dict.items()}
print("\nAssignment 12:", swapped_dict)

# ==========================
# Assignment 13: Default Dictionary
# ==========================
from collections import defaultdict

dd = defaultdict(list)
dd["Python"].append("Variables")
dd["Python"].append("Loops")
dd["SQL"].append("SELECT")
print("\nAssignment 13:", dict(dd))

# ==========================
# Assignment 14: Counting with Dictionaries
# ==========================
def count_characters(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print("\nAssignment 14:", count_characters("hello"))

# ==========================
# Assignment 15: Dictionary and JSON
# ==========================
import json

book = {
    "title": "Python Basics",
    "author": "John Doe",
    "year": 2024,
    "genre": "Programming"
}

json_string = json.dumps(book)
print("\nAssignment 15:", json_string)