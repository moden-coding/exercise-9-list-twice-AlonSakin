l = []

while n := int(input("New item: ")):
    l.append(n)
    print(f"The list now: {l}")
    print(f"The list in order: {sorted(l)}")
print("Bye!")