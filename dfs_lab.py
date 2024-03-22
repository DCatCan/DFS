
#Author Danilo Catalan Canales
import numpy as np


#states of visited vertices
NodeStates = {
    "white":0,
    "gray": 1,
    "black":2,
}

class vertex:
    #vertex object which has the different requisites needed to mark discoverTime, finishTime
    #stateColor, etc..
    def __init__(self, node, adj=[]):
        self.node = node
        self.color = NodeStates["white"]
        self.pred = None
        self.adj = adj
        self.d = None
        self.f = None


def adjMatrix(N):
    #This function creates an directed edge matrix with N vertices (not actual matrix but a list for each vertex with which vertex its connected to, self-loops not allowed)
    A = {}
    for i in range(0,N):
        temp = []
        for j in range(0,N):
            if i == j:
                pass
            else:
                randomNr = np.random.uniform()
                if randomNr <= 0.15:
                    temp.append(j)
                else:
                    pass  
        A[i] = temp
    return A
    


class graph:
    #creates a graph with a predetermined adjecency matrix with 10 vertices for a directed graph. 
    def __init__(self):
        #initializes the directed graph G with the directed edges and attaches them to 
        #the corresponding vertex object
        eMatrix = adjMatrix(10)
        self.E = eMatrix
        self.V = [vertex(x, eMatrix[x]) for x in range(0,10)]
        self.nodeArr = []

    def getE(self):
        return self.E
    def getV(self):
        return self.V
    def getVertex(self, u):
        return self.V[u]
    
    def topoHelp(self, node, visited, stack):
        #topological recursive help function to go through the vertices 
        #and check which ones have been visited.
        visited.add(node)
        stack.add(node)

        for neighborInd in node.adj:
            neighbor = self.getVertex(neighborInd)
            if neighbor not in visited:
                if self.topoHelp(neighbor, visited, stack):
                    return True
            elif neighbor in stack:
                return True

        stack.remove(node)
        return False
    
    def topoSort(self):
        #Goes through all vertices, if there is a back-edge then the function returns
        #false since its cyclic and if true its acyclic. 
        visited = set()
        stack = set()
        for node in self.getV():
                if node not in visited:
                    if self.topoHelp(node, visited, stack):
                        return False        
        return True




t = 0
def dfs(G):
    #dfs start method with initial values, t is 0 when called again.
    global t
    t = 0
    for u in G.getV():
        if u.color == NodeStates["white"]:
            dfs_visit(G,u)


            

def dfs_visit(G,u):
    #dfs recursive help function 
    global t
    t = t + 1
    u.d = t
    u.color = NodeStates["gray"]
    for v in u.adj:
        if G.getVertex(v).color == NodeStates["white"]:
            G.getVertex(v).pred = u
            dfs_visit(G, G.getVertex(v))
     
    u.color = NodeStates["black"]
    t = t+1
    u.f = t
    G.nodeArr.append(u)






def main():
    # The main function initializes all parameters, m tells how many times it should repeat
    # the process. totAcyclic and totCyclic are the amount of acyclic and cyclic graphs that are created with a 0.15 probability rate
    # of having two vertices connected, independent of each other.
    m = 1000
    totAcyclic = 0
    totCyclic = 0
    for i in range(0,m):
        G = graph()
        dfs(G)
        if G.topoSort():
            totAcyclic+=1
        else:
            totCyclic+=1

    print("Cyclic graphs: " + str(totCyclic))
    print("Acyclic graphs: " + str(totAcyclic))

    cyclicAvg = totCyclic/m
    acyclicAvg = totAcyclic/m

    print("Cyclic Avg: " + str(cyclicAvg))
    print("Acyclic Avg: " + str(acyclicAvg))



    


    return 0


if __name__ == "__main__":
    main()
