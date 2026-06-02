# 1. Conditionals (if-elif-else)
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"Grade evaluated to: {grade}")

# 2. While Loop (Runs until a condition becomes False)
counter = 3
while counter > 0:
    print(f"Countdown: {counter}")
    counter -= 1  # Infinite loop safeguard

# 3. For Loop & Range (Definite iteration)
print("Iterating over a range:")
for i in range(1, 4):  # Starts at 1, stops BEFORE 4
    print(f"Iteration {i}")

# 4. Loop Control: break and continue
print("Testing loop control:")
for num in range(1, 6):
    if num == 2:
        continue  # Skips 2 entirely, jumps to next iteration
    if num == 5:
        break     # Aborts the entire loop instantly
    print(f"Processing number: {num}")