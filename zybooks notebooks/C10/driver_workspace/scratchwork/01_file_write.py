"""4/23 - writing to a file.
Three steps: open() -> write() -> close().
Mode 'w' creates or overwrites.
"""
outfile = open("customers.txt", "w")
outfile.write("Bruno
")
outfile.write("Alice
")
outfile.write("Chen
")
outfile.close()
print("Wrote 3 lines to customers.txt")
print("---- file contents ----")
with open("customers.txt") as f:
    print(f.read())