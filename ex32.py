#list V
#tuple?

the_count = [1,2,3,4,5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}.")

for fruit in fruits:
    print(fruit)

for x in change:
    print(x)
    # Using {} caose don't know this is number or string
    print(f"This is {x}")

elements = []

for i in range(1, 6): # don't include 6, the last word!
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Elements was: {i}")

