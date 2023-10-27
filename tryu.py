
n =4
m =5
t =20
ldt =[[1,2,15,20],[1,3,1,6],[2,4,25,30],[3,4,2,7],[3,4,30,35]]
dic={}
for x in ldt:
    if x[0] not in dic.keys():
        dic[x[0]] =[x]
    else:
        dic[x[0]].append(x)
def ats(dic ):
    visited =[]
    queue =[]
    time =0
    queue.append([1,0])
    sum=0

    while queue!=[]:
        time+=t
        s = queue.pop(0)

        if s[0] == n:
            return "YES",s[1]
        ap = dic[s[0]]
        for x in ap:
            if x[1] not in visited:
                if x[2] < time:
                    visited.append([x[1],x[-1]])
            for y in range(0,len(visited)):
                    if visited[y][0] == x[1] and visited[y][1] >  x[2] :
                        visited[y][-1] = x[1]




        print(visited)
ats(dic)