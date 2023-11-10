from queue import PriorityQueue
v=14
graph=[[]for i in range(v)]
def best_first_search(actual_Src, target, n):
    visited=[False]*n
    pq=PriorityQueue()
    pq.put((0,actual_Src))
    visited[actual_Src]=True
    while pq.empty()==False:
        u=pq.get()[1]
        print(u,end="" )
        if u==target:
            break
    
        for v,c in graph[u]:
            if visited[v]==False:
                visited[v]=True
                pq.put((c,v))
        print()
def addedge(x,y,heuristic):
    graph[x].append((y,heuristic))
    graph[y].append((x,heuristic))
addedge(0,1,4)
addedge(0,2,2)
addedge(1,3,11)
addedge(1,4,1)
addedge(2,5,13)
addedge(2,6,12) 
source=0
target=5
best_first_search(source, target, v)

        
    
    
    

