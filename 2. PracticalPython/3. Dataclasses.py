# A dataclass is a convenient way to create classes mainly used for storing data. Python generates common methods for you, including an initializer.

# Without a dataclass, you often write an initializer manually.
# With a dataclass:

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool


item = Product("Keyboard", 1499.0, True)

print(item.name)
print(item.price)
print(item.in_stock)

print(item)
