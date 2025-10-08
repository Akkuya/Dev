t = int(input())
out = ""
for i in range(t):
    n = int(input())
    mx = 0
    for i in range(n):
        x = int(input())
        if x > mx:
            mx = x
    