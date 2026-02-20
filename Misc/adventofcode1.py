count = 0
with open("input.txt") as f:
    curr = 50
    data = f.read().splitlines()
    for i in range(4333):
        cmd = (data[i][0], int(data[i][1:]))
        if cmd[0] == "R":
            curr += cmd[1]
        else:
            curr -= cmd[1]
    
        curr = curr%100
        if curr == 0:
            count += 1
    print(count)