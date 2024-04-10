with open("./saved_models/predictions.txt") as f:
    lines = f.readlines()

count = 0
for i in range(0, len(lines), 2):
    a = eval(lines[i].split()[1])
    b = eval(lines[i + 1].split()[1])
    if a != b:
        count += 1
print (count)
