priorities = [2, 1, 3, 2]
location = 2

cnt = 0
pre = -1
goal = priorities[location]
length = len(priorities)
for i in range(9,0,-1):
    if i not in priorities:
        continue
    if goal == i and pre == -1:
        cnt = priorities[0:location + 1].count(i)
        print(cnt)
    for j in range(pre,pre+length):
        if priorities[j%length] == i:     
            cnt += 1
            pre = j % length
        if i == goal and j%length == location:
            print(cnt)