from collections import defaultdict

class Graph:
    def __init__(self):
        self.connected_city =defaultdict(list)
        self.city = set()
       
    def addEdge(self, v, w):
        self.connected_city[v].append(w)
        self.connected_city[w].append(v)
        self.city.add(v)
        self.city.add(w)
       
    def DFS(self, v, visited):
        visited[v] = True
       
        for i in self.connected_city[v]:
            if (not visited[i]):
                self.DFS(i, visited)


    def number_of_flight(self, cities):
   
        self.city.union(cities)
        visited  = { i:False for i in  self.city.union(cities)}
       
        count = 0
        for city in cities:
            if not visited[city]:
                self.DFS(city, visited)
                count +=1
   
        return count


if __name__ == '__main__':
    g = Graph()
    for edge in [("c1", "c2"),("c2", "c6"),("c6", "c8"), ("c4", "c5"), ("c3", "c6")]:
        g.addEdge(edge[0], edge[1])


    print(g.number_of_flight(('c1', 'c6', 'c8', 'c11')))
