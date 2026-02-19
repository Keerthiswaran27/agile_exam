import sys
import os

# Safe parameter handling
# If an argument is passed, use it; otherwise, use a placeholder
str1 = sys.argv[1] if len(sys.argv) > 1 else "No_Parameter_Passed"

print("=================================")
print("Processing Parameter:", str1)
print("=================================")

# Task 2: Rename logic for Experiment 5
old_name = "sample.txt"
new_name = "newfile.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"Success: {old_name} has been renamed to {new_name}")
else:
    print(f"Error: {old_name} not found in workspace.")