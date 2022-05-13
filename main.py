candidates = {"A": 0, "B": 0, "C": 0}
unacceptable = 0
voters = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]

for i in voters:
    vote = input("Enter {} candidate : ".format(i))
    if vote == "A":
        candidates["A"] += 1

    elif vote == "B":
        candidates["B"] += 1

    elif vote == "C":
        candidates["C"] += 1

    else:
        unacceptable += 1
        print("Vote can't recognize")

print(candidates)
print(unacceptable)