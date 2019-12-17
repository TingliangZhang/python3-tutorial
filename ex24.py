print("Let's practice everything.")
print("You\' need to knoe \'bout escapes with \\ that do:")
print('\n newlines and \t tabs')

poem = """
\t Tina
with big eyes\n love study
"""

print("-----------")
print(poem)
print("-----------")


five = 10-2+3-6
print(f"This should be five: {five}")

def secret(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret(start_point)

print("Starting with{}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point/10

formula=secret(start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
