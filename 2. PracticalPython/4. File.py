# File handling lets your program read information from files and write information to them.

with open("learning.txt", "w", encoding="utf-8") as file:
    file.write("Today I learned Python file handling.")    # check the 'learning.txt' file is created on root folder

with open("learning.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# Understand the modes:

    # "w" — write; creates the file or replaces its existing contents.
    # "r" — read an existing file.
    # "a" — append content to the end of a file.

# "with" automatically closes the file when the block finishes, even if an error occurs.