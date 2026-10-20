def greet():
  print("Hello World")

greet()
print("----")

# A. Parameters and arguments

def greet(name):
  print(f"Hello {name}!")

greet("Mahesh")
print("----")

# B. Return values

def add(a, b):
  return a + b

result = add(5,8)
print(result)
print("----")

# C. Default parameters

def greet(name, language = "Python"):
  return f"{name} ia learning {language}"

print(greet("Mahesh"))
print(greet("Mahesh", "Java"))
print("----")

# D. Keyword arguments

def employee(name, salary):
  print(name, salary)

employee(name = "Mahesh", salary=50000)
print("----")

# When to use: Whenever you want to reuse logic, such as calculating salaries, validating job eligibility, or processing API data.
