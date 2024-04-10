import json

with open("./f_en_mu.txt") as f:
    lines = f.readlines()

def getname(identi):
    s = ""
    for i in range(len(identi)):
        c = identi[i]
        if s == "" and c.lower() >= 'a' and c.lower() <= 'z':
            s += c
        if s != "":
            if (c.lower() >= 'a' and c.lower() <= 'z') or (c >= '0' and c <= '9'):
                s += c
            else:
                break
    return s
    
def getdumps(code, idx):
    dic = {}
    dic["project"] = "-"
    dic["commit_id"] = "2312312"
    dic["target"] = 0
    dic["func"] = code
    dic["idx"] = idx
    return json.dumps(dic)

with open("./input.jsonl", "w") as f:
    count = 0 
    for line in lines:
        data = json.loads(line)
        ori = data[0]
        new = data[1]
        identi = data[2]
        identi = getname(identi)
        new = new.replace("<extra_id_0>", identi)
        if ori.strip() != new.strip():
#            f.write(json.dumps([ori.strip(), new.strip()]) + "\n")
#            f.write(new.strip() + "\n")
            f.write(getdumps(ori.strip(), count) + "\n")
            count += 1
            f.write(getdumps(new.strip(), count) + "\n")
            count += 1

