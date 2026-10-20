employee = {
    "name" : "Mahesh",
    "age" : 27,
    "role" : "Java Developer"
}
print(employee);
print(employee["name"])
print(employee["age"])
print(employee["role"])
print("----")

# Add, update, and delete

employee['salary'] = 50000
employee['age'] = 28

del employee["role"]

print(employee)
print("----")

# Useful dictionary methods

print(employee.keys())  # All Keys
print(employee.values()) # All Values
print(employee.items()) # Key-value pairs
print(employee.get("name")) # Mahesh
print(employee.get("city")) # None

# get() is useful when a key might not exist. Unlike employee["city"], it can return a default value without raising a KeyError.

# When to use: Representing structured records such as employees, job postings, API responses, and configuration settings.
