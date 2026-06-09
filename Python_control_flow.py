# Module 2: Control Flow Assignments
## Lesson 2.1: Conditional Statements
### Assignment 1: Simple if Statement

# <!-- Write a program that asks the user to input a number and prints whether the number is positive. -->

# answer:


# n = int(input())
# if n % 2 == 0:
#     print(n)

### Assignment 2: if-else Statement
# Write a program that asks the user to input a number and prints whether the number is positive or negative.


# n = int(input())
# if n% 2 == 0:
#     print("Positive")
# else:
#     print("Negative")

# ### Assignment 3: if-elif-else Statement

# Write a program that asks the user to input a number and prints whether the number is positive, negative, or zero.


# n = int(input())
# if n == 0:
#     print("zero")
# elif n% 2 == 0:
#     print("Positive")
# else:
#     print("Negative")

# ### Assignment 4: Nested if Statement

# Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative.


# n = int(input())

# if n > 0:
#     if n % 2 == 0:
#         print("Positive and even")
#     else:
#         print("Positive and odd")
# elif n < 0:
#     if n % 2 == 0:
#         print("Negative and even")
#     else:
#         print("Negative and odd")
    

# ## Lesson 2.2: Loops
# ### Assignment 5: for Loop

# Write a program that prints all the numbers from 1 to 10 using a for loop.

# n = int(input())
# for i in range(1,n+1):
#     print(i)


# ### Assignment 6: while Loop

# Write a program that prints all the numbers from 1 to 10 using a while loop.


# n = int(input())
# i = 0
# while i< n:
#     i = i +1
#     print(i)

# ### Assignment 7: Nested Loops

# Write a program that prints a 5x5 grid of asterisks (*) using nested loops.

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*", end="")
#     print()

# ### Assignment 8: break Statement

# Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.

# total = 0

# while True:
#     num = int(input())
#     if num == 0:
#         break
#     total += num
# print(total)


# ### Assignment 9: continue Statement

# Write a program that prints all the numbers from 1 to 10 except 5 using a for loop and continue statement.

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)


# ### Assignment 10: pass Statement

# Write a program that defines an empty function using the pass statement.

# def empty_function():
#     pass

# ### Assignment 11: Combining Loops and Conditionals

# Write a program that asks the user to input a number and prints all the even numbers from 1 to that number using a for loop.

# n = int(input())
# for i in range(1, n+1):
#     if i % 2 == 0:
#         print(i)    


# ### Assignment 12: Factorial Calculation

# n = int(input())
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)


# Write a program that calculates the factorial of a number input by the user using a while loop.


# n = int(input())
# fact = 1
# i = 1
# while i <= n:
#     fact = fact * i
#     i = i + 1
# print(fact)     


# ### Assignment 13: Sum of Digits

# Write a program that calculates the sum of the digits of a number input by the user using a while loop.

# num = int(input())
# total = 0

# while num > 0:
#     digit = num % 10
#     total += digit
#     num = num // 10

# print(total)


# ### Assignment 14: Prime Number Check

# Write a program that checks if a number input by the user is a prime number using a for loop.

# num = int(input())

# if num <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")



# ### Assignment 15: Fibonacci Sequence

# Write a program that prints the first n Fibonacci numbers, where n is input by the user. -->

# n = int(input())

# a, b = 0, 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
