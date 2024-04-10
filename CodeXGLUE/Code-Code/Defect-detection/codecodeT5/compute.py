with open("./saved_models/predictions.txt") as f:
    lines = f.readlines()

count = 0
oricount = 0
mutcount = 0
diff = 0

for i in range(0, len(lines), 2):
    ori = eval(lines[i].split()[1])
    mut = eval(lines[i + 1].split()[1])
    count += 1
    oricount += ori
    mutcount += 1 - mut
    if ori == mut and ori == 0:
        diff += 1


print ("ori acc:", 1 - oricount/count)
print ("mut acc:", mutcount/count)
print ("issue num:", mutcount)
print ("count number:", count)
print ("diff:", diff)
