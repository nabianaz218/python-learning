# 1. Variable Assignment
user_name = "Nabia"  # String (str)
age = 23             # Integer (int)
gpa = 3.8            # Floating-point (float)
is_learning = True   # Boolean (bool)

# 2. Type Checking
print(f"Variable types: name={type(user_name)}, age={type(age)}, gpa={type(gpa)}")

# 3. Type Casting (Converting types)
# Crucial for user inputs which always come in as strings
input_years = "5"
calculated_years = int(input_years) + 2
print(f"Casted string to int for calculation: {calculated_years}")

# 4. String Manipulation
greeting = "  hello world  "
print(greeting.strip().capitalize())  # Cleans whitespace and capitalizes: "Hello world"