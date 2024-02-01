from collections import defaultdict

class Graph:
 
 def __init__(self):
   
   self.graph = defaultdict(list)

 def addEdge(self,u,v):
   
   self.graph[u].append((v))
   self.graph[v].append((u))

 def dispg(self):
   
   print(self.graph.items())

 def BFS(self, s,goal):
    
    visited = [False] * (len(self.graph))
    frontier_q = []
    frontier_q.append(s)
    visited[s] = True

    while frontier_q:

      s = frontier_q.pop(0)
      print (s, end = " ")

      if(s == goal):

        print("\n Goal found")

        return
      
      for i in self.graph[s]:

        if visited[i] == False:

          frontier_q.append(i)
          visited[i] = True
          print("\n Goal not found")


g = Graph()

g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(3,5)
g.dispg()
print ("Following is Breadth First Traversal (starting from vertex 1)")
g.BFS(1,4)

