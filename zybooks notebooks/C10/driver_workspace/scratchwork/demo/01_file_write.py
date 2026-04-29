"""4/23 - writing to a file.
Three steps: open() -> write() -> close().
Mode 'w' creates or overwrites.
"""
outfile = open("demo/customers.txt", "w")
outfile.write("Bruno\n")
outfile.write("Alice\n")
outfile.write("Chen\n")
outfile.close()
print("Wrote 3 lines to demo/customers.txt")
print("---- file contents ----")
with open("demo/customers.txt") as f:
    print(f.read())