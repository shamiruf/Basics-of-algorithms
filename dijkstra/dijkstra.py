class Vertex:
    def __init__(self, id, name):
        self.id = id 
        self.name = name
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None
        self.visited = False

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight 


class Dijkstra:
    def __init__(self):
        self.vertexes = []


    def computePath(self, sourceId):
        queue = []

        for cur_vertex in self.vertexes:
            if sourceId == cur_vertex.id:
                cur_vertex.minDistance = 0
                queue.insert(0, cur_vertex)
            else:
                queue.append(cur_vertex)
        
        while queue:
            cur_vertex = queue.pop(0)
            for edge in cur_vertex.edges:
                trgt = edge.target
                #print("TARGET IIIISSS : " + str(trgt))
                for t_vertex in self.vertexes:
                    if t_vertex.id == trgt:
                        #print("T_VERTEX min d: " + str(t_vertex.minDistance))
                        #print("CUR_VERTEX min d: " + str(i.minDistance))
                        #print("EDGEE WEIGHT: " + str(edge.weight))
                        if t_vertex.minDistance > (cur_vertex.minDistance + edge.weight):
                            t_vertex.minDistance = cur_vertex.minDistance + edge.weight
                            t_vertex.previousVertex = cur_vertex

            
            for element in range(len(queue)):
                try:
                    if queue[element].minDistance > queue[element + 1].minDistance:
                        x = queue[element + 1]
                        queue[element + 1] = queue[element]
                        queue[element] = x
                except IndexError:
                    break
            
    def getShortestPathTo(self, targetId):
        listOfVertexes = []

        for vertex in self.vertexes:
            if vertex.id == targetId:
                trgt = vertex
                listOfVertexes.append(trgt)
        
        for vertex in self.vertexes:
            if vertex == trgt.previousVertex:
                listOfVertexes.append(vertex)
                trgt = trgt.previousVertex
        listOfVertexes.reverse()
        return listOfVertexes

    def createGraph(self, vertexes, edgesToVertexes):
        
        self.vertexes = vertexes

        for vertex in vertexes:
            for edge in edgesToVertexes:
                if edge.source == vertex.id:
                    vertex.edges.append(edge)

    def printD(self):
        for i in self.vertexes:
            print(i.name)
            for x in i.edges:
                print(x.weight)
        
    def resetDijkstra(self):
        for v in self.vertexes:
            v.minDistance = float('inf')
            v.previousVertex = None

    def getVertexes(self):
        return self.vertexes


#Test graph
vertexes = [
  Vertex(0, 'Redville'),
  Vertex(1, 'Blueville'),
  Vertex(2, 'Greenville'),
  Vertex(3, 'Orangeville'),
  Vertex(4, 'Purpleville')
]
edges = [
  Edge(0, 1, 5),
  Edge(0, 2, 10),
  Edge(0, 3, 8),
  Edge(1, 0, 5),
  Edge(1, 2, 3),
  Edge(1, 4, 7),
  Edge(2, 0, 10),
  Edge(2, 1, 3),
  Edge(3, 0, 8),
  Edge(3, 4, 2),
  Edge(4, 1, 7),
  Edge(4, 3, 2)
]
#New Dijkstra created
dijkstra = Dijkstra()
#Graph created
dijkstra.createGraph(vertexes,edges)
#Getting all vertexes
dijkstraVertexes = dijkstra.getVertexes()
#Computing min distance for each vertex in graph
for vertexToCompute in dijkstraVertexes:
    dijkstra.computePath(vertexToCompute.id)
    print('Printing min distance from vertex:'+str(vertexToCompute.name))
    #Print minDitance from current vertex to each other
    for vertex in dijkstraVertexes:
        print('Min distance to:'+str(vertex.name)+' is: '+str(vertex.minDistance))
    #Reset Dijkstra between counting
    dijkstra.resetDijkstra()
#Distance with path
for vertexToCompute in dijkstraVertexes:
    dijkstra.computePath(vertexToCompute.id)
    print('Printing min distance from vertex:'+str(vertexToCompute.name))
    #Print minDitance and path from current vertex to each other
    for vertex in dijkstraVertexes:
        print('Min distance to:'+str(vertex.name)+' is: '+str(vertex.minDistance))
        print('Path is:',end=" ")
        #Get shortest path to target vertex
        path = dijkstra.getShortestPathTo(vertex.id)
        for vertexInPath in path:
            print(str(vertexInPath.name),end=" ")
        print()
    #Reset Dijkstra between counting
    dijkstra.resetDijkstra()