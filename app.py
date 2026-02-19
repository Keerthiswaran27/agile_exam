import sys
import os

# 1. Safe Parameter Handling (Prevents IndexError)
str1 = sys.argv[1] if len(sys.argv) > 1 else "Experiment_User"
print(f"Processing for user: {str1}")

# 2. File Deletion Logic (Experiment 5: Version 4)
target_file = "newfile.txt"

if os.path.exists(target_file):
    os.remove(target_file)
    print(f"Task 2 Success: {target_file} has been deleted.")
else:
    # If the file isn't there, we create a temporary one and then delete it 
    # just to demonstrate the code works
    print(f"Note: {target_file} not found. Creating and deleting a temp file.")
    with open(target_file, "w") as f:
        f.write("temporary")
    os.remove(target_file)
    print("Temporary file created and deleted successfully.")

print("Task 3: Workspace is now clean.")