#String and Text
people = 10
x=f"There are {people} people"
binary="binary"
do_not="don't"
y=f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = True
joke_evaluation="Is this joke funny?    {}"

print(joke_evaluation.format(hilarious))

w="I am "
e="me"
print(w + e)