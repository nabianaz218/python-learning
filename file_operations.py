# Practicing File Input and Output (I/O) in Python

# 1. Writing to a file ('w' mode overwrites existing content)
with open("sample.txt", "w") as file:
    file.write("Hello! This file was created dynamically by Python.\n")
    file.write("File handling allows us to store data permanently.\n")
print("Successfully written data to sample.txt!")

# 2. Appending to a file ('a' mode adds text to the end without deleting)
with open("sample.txt", "a") as file:
    file.write("This line was appended later using 'a' mode.\n")
print("Successfully appended new data!")

# 3. Reading from a file ('r' mode)
print("\n--- Reading file contents line by line using a loop ---")
with open("sample.txt", "r") as file:
    # We can loop directly through the file object!
    for line in file:
        # .strip() removes the extra newline character from print()
        print(line.strip())
        