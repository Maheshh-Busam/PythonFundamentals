age = 22

if(age >= 18):
  print("Eligible")
else:
  print("Not Eligible")
print("----")

# Multiple conditions

score = 75

if score >= 90:
  print("Grade A")
elif score >= 70:
  print("Grade B")
elif score >= 50:
  print("Grade C")
else:
  print("Fail")
print("----")

# Comparison and logical operators
#
# ==	  Equal
# !=	  Not equal
# > / <	Greater / less
# >= / <=	Greater/less than or equal
# and	  Both conditions must be true
# or	  At least one must be true
# not	  Reverses a Boolean value

age = 25
experrience = 3

if age >= 18 and experrience >= 2:
  print("Eligible for this role")
