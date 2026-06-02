# ==============================================================================
# 📦 PYTHON'S MOST POPULAR BUILT-IN MODULES REFERENCE GUIDE
# ==============================================================================
# A module is just a pre-written file containing code made by experts. 
# Instead of reinventing the wheel, we import them to do heavy lifting for us!
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. THE 'random' MODULE
# Simple Definition: Used when you need unpredictability, luck, or choice in a program.
# Common Use Cases: Games (dice rolls), shuffling data, picking random winners.
# ------------------------------------------------------------------------------
import random

print("--- 1. Random Module Examples ---")
print(f"Random decimal between 0 and 1: {random.random()}")
print(f"Random whole number between 1 and 10: {random.randint(1, 10)}")

items = ['apple', 'banana', 'cherry']
print(f"Random choice from a list: {random.choice(items)}")


# ------------------------------------------------------------------------------
# 2. THE 'math' MODULE
# Simple Definition: Gives you access to advanced mathematical formulas and constants.
# Common Use Cases: Trigonometry, square roots, rounding numbers up or down.
# ------------------------------------------------------------------------------
import math

print("\n--- 2. Math Module Examples ---")
print(f"The exact value of Pi: {math.pi}")
print(f"Square root of 64: {math.sqrt(64)}")
print(f"Round UP 4.1 to nearest whole number: {math.ceil(4.1)}")


# ------------------------------------------------------------------------------
# 3. THE 'os' MODULE (Operating System)
# Simple Definition: Lets your Python script talk directly to your computer's folders and files.
# Common Use Cases: Creating folders, deleting files, checking what folder you are currently in.
# ------------------------------------------------------------------------------
import os

print("\n--- 3. OS Module Examples ---")
print(f"Current folder path you are working in: {os.getcwd()}")
print(f"List of all files in this folder: {os.listdir('.')}")


# ------------------------------------------------------------------------------
# 4. THE 'sys' MODULE (System)
# Simple Definition: Controls the Python environment itself and interacts with the terminal window.
# Common Use Cases: Reading inputs directly from the command line, shutting down a script forcefully.
# ------------------------------------------------------------------------------
import sys

print("\n--- 4. Sys Module Examples ---")
print(f"Python version currently running: {sys.version}")
# sys.exit()  # <-- Running this line would instantly crash/stop the program!


# ------------------------------------------------------------------------------
# 5. THE 'datetime' MODULE
# Simple Definition: Used to track, calculate, and format dates and times.
# Common Use Cases: Timestamps on user posts, calculating age, setting alarms.
# ------------------------------------------------------------------------------
import datetime

print("\n--- 5. Datetime Module Examples ---")
current_time = datetime.datetime.now()
print(f"Exact date and time right now: {current_time}")
print(f"Formatted human-readable date: {current_time.strftime('%A, %B %d, %Y')}")


# ------------------------------------------------------------------------------
# 6. THE 'json' MODULE
# Simple Definition: Converts Python data (like dictionaries) into a universal text format 
# that web browsers and external databases understand.
# Common Use Cases: Saving game settings, fetching data from internet websites (APIs).
# ------------------------------------------------------------------------------
import json

print("\n--- 6. JSON Module Examples ---")
python_dict = {"name": "Nabia", "role": "Developer"}
json_string = json.dumps(python_dict)  # Converts dictionary to a single string text

print(f"Data converted to web-friendly JSON string: {json_string}")
print(f"Data type is now: {type(json_string)}")