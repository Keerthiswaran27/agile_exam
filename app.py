import sys

str1 = sys.argv[1]

print("=================================")
print("String Concatenation Result")
print("=================================")
print("parameter String :", str1)


# Added Logic
suffix = "_PROCESSED"
concatenated_str = str1 + suffix
char_count = len(str1)

print(f"Concatenated with suffix: {concatenated_str}")
print(f"Original string length: {char_count}")
print(f"Uppercase version: {str1.upper()}")
print(f"Visual Pattern: {'*' * char_count}")

# --- Final 5 lines starts here ---
is_alpha = str1.isalnum()
reversed_str = str1[::-1]

print(f"Reversed String: {reversed_str}")
print(f"Is Alphanumeric: {is_alpha}")
print("Status: Execution Successful")