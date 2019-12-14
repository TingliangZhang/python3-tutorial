# $ python ex16.py ex16_test.txt

from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("If you don't want thar, hit CTRL-C or ^C.")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

#Clear the File
print("Truncating the file. Goodbye!")
target.truncate()

print("Input three lines")

line1=input("line 1: ")
line2=input("line 2: ")
line3=input("line 3: ")

print("Writing these to the file.")

target.write(f"{line1}\n{line2}\n{line3}")

print("Closing it")
target.close()