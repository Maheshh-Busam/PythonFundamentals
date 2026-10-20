# A. for loop -- Use it to iterate over a collection or a sequence.

skills = ["java", "python", "SQL"]

for skill in skills:
  print(skill)
print("----")

# B. range() -- range(start, stop, step) generates a sequence of integers. The stop value is excluded.

for i in range(1,6):
  print(i);
print("----")

# C. while loop -- Repeats while a condition remains true.

count = 1

while count <= 3:
  print(count)
  count += 1
print("----")

# D. break and continue -- break stops the loop and continue skips the current iteration and proceeds to the next one.

# break
for i in range(1,6):
  if i == 3:
    break;
  print(i)
print("----")

# continue

for i in range(1,6):
  if i == 3:
    continue
  print(i)
print("----")
