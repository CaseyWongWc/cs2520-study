"""4/23 - appending to a file.
Mode 'a' keeps existing content. Run 01_file_write.py first.
"""
outfile = open("customers.txt", "a")
outfile.write("Sam\n")
outfile.write("Dana\n")
outfile.close()

print("Appended 2 lines.")
with open("customers.txt") as f:
    print(f.read())
