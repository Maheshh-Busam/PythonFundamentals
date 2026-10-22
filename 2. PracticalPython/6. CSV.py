# CSV stands for Comma-Separated Values. It stores tabular data, similar to an Excel spreadsheet.

# First, create courses.csv:

import csv

# To read a CSV file:
with open("courses.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["level"])

# Each row behaves like a dictionary, with column names as keys.
# ---------------------------------------------------------

# To write a CSV file:

with open("results.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Course", "Score"])
    writer.writerow(["Python", 90])
    writer.writerow(["SQL", 85])

# # check the 'results.csv' file is created on root folder