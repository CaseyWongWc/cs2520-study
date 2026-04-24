"""4/23 - handling numeric data with files.
Files store STRINGS. Convert both directions:
  write:  str(num)
  read:   int(s) / float(s)
"""
prices = [9.99, 14.50, 3.25]
out = open("prices.txt", "w")
for p in prices:
    out.write(str(p) + "\n")
out.close()

total = 0.0
with open("prices.txt") as f:
    for line in f:
        total += float(line.strip())
print("Total: $", total)
