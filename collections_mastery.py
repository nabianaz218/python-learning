# 1. Lists (Ordered, mutable, allows duplicates)
todo_list = ["code", "read"]
todo_list.append("exercise")  # Adds item to the very end
print(f"List after append: {todo_list}")

# 2. Tuples (Ordered, IMMUTABLE - cannot change once created)
coordinates = (10.5, 20.3)
# coordinates[0] = 15.0  # ❌ This will crash! Tuples don't support item assignment.

# 3. Dictionaries (Key-Value pairs, fast lookup, unique keys)
user_profile = {"username": "coder1", "status": "active"}
user_profile["status"] = "offline"  # Updating a single value using brackets
print(f"Updated dictionary: {user_profile}")

# Looping correctly using .items()
for key, value in user_profile.items():
    print(f"Key: {key} -> Value: {value}")

# 4. Dictionary Comprehension (Modern syntax)
prices_usd = {"milk": 2, "bread": 3}
prices_doubled = {item: price * 2 for item, price in prices_usd.items()}
print(f"Doubled prices: {prices_doubled}")