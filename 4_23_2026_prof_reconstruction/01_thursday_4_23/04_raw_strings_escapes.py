"""4/23 - raw strings and escape characters.
Windows paths break because \ is an escape char. Three fixes:
"""
path_raw = r"C:\Users\Bronco\Documents\Python\notes.txt"
print("raw   :", path_raw)

path_esc = "C:\\Users\\Bronco\\Documents\\Python\\notes.txt"
print("esc   :", path_esc)

path_fwd = "C:/Users/Bronco/Documents/Python/notes.txt"
print("fwd   :", path_fwd)

print("\nCommon escapes:")
print("tab\there")
print("newline:\nhere")
print("quote: \"double\" and 'single'")
print("backslash: \\")
