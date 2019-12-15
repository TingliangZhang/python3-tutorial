# $ New-Item ex20_Test.txt
# $ python ex20.py .\ex20_Test.txt

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    # readline()输出自带 \n print也会输出 \n So end="" needed
    print(line_count, f.readline(), end="")

current_file=open(input_file)

print_all(current_file)

rewind(current_file)

current_line=1
print_a_line(current_line, current_file)

current_line= current_line +1
print_a_line(current_line, current_file,)

current_line += 1
print_a_line(current_line, current_file)