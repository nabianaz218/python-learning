# Import built-in modules to extend Python's core power
import random


# 1. Basic Function with parameters and return value
def calculate_tax(price, tax_rate=0.05):  # tax_rate has a default argument
    """Calculates total price including tax."""
    return price + (price * tax_rate)


# 2. Dynamic Arguments (*args and **kwargs)
def print_user_summary(name, *hobbies, **additional_info):
    """
    *args captures extra positional arguments as a Tuple.
    **kwargs captures extra keyword arguments as a Dictionary.
    """
    print(f"\nUser: {name}")
    print(f"Hobbies (Tuple): {hobbies}")
    print(f"Metadata (Dict): {additional_info}")


# Execution
final_price = calculate_tax(100)  # Uses default tax
print(f"Final calculated price: {final_price}")

print_user_summary("Alice", "Chess", "Coding", "Gaming", location="Pakistan", role="Student")