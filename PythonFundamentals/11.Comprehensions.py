# A. List comprehension
# Normal approach:
numbers = [1,2,3,4,5]
squares = []

for n in numbers:
  squares.append(n * n)

print(numbers)
print(squares)
print("----")

# Using list comprehension:

numbers = [1,2,3,4,5]
squares = [n * n for n in numbers]  # Syntax -- [expression for item in iterable]

print(numbers)
print(squares)
print("----")

# B. List comprehension with a condition

# Get only even numbers:
numbers = [1,2,3,4,5,6]
even_numbers = [n for n in numbers if n % 2 == 0]

print(numbers)
print(even_numbers)

# C. Set comprehension

numbers = [1,2,2,3,3,4]
unique_squares = {n * n for n in numbers}

print(numbers)
print(unique_squares)
print("----")

# D. Dictionary comprehension
numbers = [1,2,3,4]
squares = {n : n * n for n in numbers}

print(numbers)
print(squares)
print("----")
