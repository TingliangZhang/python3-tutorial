people=30
cars=40
trucks=15


if cars > people:
    print("Take cars!")
elif cars < people:
    print("should not take cars!")
else:
    print("cannot decide")

if trucks > cars:
    print("too many trucks")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("cannot decide")

if people>trucks:
    print("Let's just take the trucks")
else:
    print("Just stay at home!!!!!!")