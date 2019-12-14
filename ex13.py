from sys import argv
# $ python ex13.py first 2nd 3rd 
script, first, second, third = argv

print("The script is called: ", script)
print("Your firsr variable is", first)
print("Your second variable is", second)
print("Your third variable is", third)

# If   Traceback (most recent call last):
#      ValueError: not enough values to unpack (expected 4, got 1)
#参数数量不足