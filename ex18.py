#Function!~
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("Nothing here!")

print_two("Tina", "Zhang")
print_two_again("Zhang", "Tina")
print_one("Tina")
print_none()