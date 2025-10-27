from collections import deque
goal = "123456780"
def show(state):
    for i in range(0,9,3):
        print(state[i:i+3].replace('0','_'))
    print("-----"
def neighbors(state):
    i = state.index("0")
    r,c = divmod(i,3)
    res=[]
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<3 and 0<=nc<3:
            j=nr*3+nc
            s=list(state)
            s[i],s[j]=s[j],s[i]
            res.append("".join(s))
    return res
def bfs(start):
    q=deque([start])
    seen={start:None}
    while q:
        s=q.popleft()
        if s==goal:
            path=[]
            while s:
                path.append(s)
                s=seen[s]
            return path[::-1]
        for n in neighbors(s):
            if n not in seen:
                seen[n]=s; q.append(n)
start="123406758"
path=bfs(start)
for p in path: show(p)



output:
123
4_6
758
-----
123
456
7_8
-----
123
456
78_

