skills = ["java", "python", "SQL"]
print(skills)
print(skills[0])
print(skills[1])
print(len(skills))
print("----")

# Common list operations

skills.append("AWS")
print(skills)
print("----")

skills.insert(1, "Spring Boot")
print(skills)
print("----")

skills.remove("SQL")
print(skills)
print("----")

last_skill = skills.pop();
print(last_skill)
print(skills)
print("----")

# Other useful operations:

numbers = [10,20,10,30]
numbers.sort()
print(numbers)
print("----")

numbers.reverse()
print(numbers)
print("----")

count_10  = numbers.count(10)
print(numbers)
print(count_10)
print(20 in numbers)
print("----")

# When to use: When you need a collection of items that you may add, remove, or modify.
