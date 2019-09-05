# Giraudo Francesco Es 33 Study Drill 5

loops = 10     # this variable replaces 6
inc = 3
numbers = []

for i in range(0,loops,inc):
    print(f"At the top i is {i}")
    numbers.append(i)
    print("Numbers now", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
