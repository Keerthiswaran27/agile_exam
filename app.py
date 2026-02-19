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