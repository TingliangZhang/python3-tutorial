def add(a,b):
    print(f"ADDING {a} +{b}")
    return a+b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

def divided(a,b):
    print(f"DIVIDING {a} / {b}")
    return a/b


age=add(10,8)
height = subtract(200,15)
weight = multiply(3,25)
iq = divided(100,10)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a Puzzle")

puzzle = add(age,subtract(height,multiply(weight,divided(iq,2))))

print(puzzle)