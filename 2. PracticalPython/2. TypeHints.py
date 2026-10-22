# Type hints indicate what kind of values a variable, parameter or function is expected to use.

# Example 1:
def calculate_area(length: float, width: float) -> float:
    return length * width

area = calculate_area(5.0, 3.0)
print(area)
print("----------")

# Read the function declaration:

    # length: float — expected to be a floating-point number.
    # width: float — expected to be a floating-point number.
    # -> float — the function is expected to return a floating-point number.

# ------------------------------------------

# Example 2:

def format_price(price: float) -> str:
    return f"Price : Rs.{price:2f}"

price = format_price(249.5)
print(price)

# Important: Type hints don't automatically validate values at runtime. They help developers, editors and static type-checking tools detect mistakes.