class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def isSafe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def mColoring(self, m, color, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, color, c):
                color[v] = c
                if self.mColoring(m, color, v + 1):
                    return True
                color[v] = 0

    def NextValue(self, m):
        color = [0] * self.V
        if not self.mColoring(m, color, 0):
            return False

        print("Solution exist and following are the assigned colors:")
        print("Room No.  ->  Color No. ")
        for c in range(0, len(color)):
            print("   ", c+1, "\t  ->\t", color[c])
        return True


g = Graph(5)
g.graph = [[0, 1, 1, 1, 0],
           [1, 0, 1, 1, 1],
           [1, 1, 0, 1, 0],
           [1, 1, 1, 0, 1],
           [0, 1, 0, 1, 0]]

m = 4   # maximum no. of colors given

print("Total no. of rooms: ", len(g.graph))
print("Total no. of color available: ", m)
print()
g.NextValue(m)

