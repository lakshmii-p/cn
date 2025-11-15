#CRC
def xor(a, b):
    r = ""
    for i in range(1, len(b)):
        r += str(int(a[i]) ^ int(b[i]))
    return r

def divide(data, key):
    pick = len(key)
    temp = data[:pick]

    while pick < len(data):
        temp = xor(key if temp[0]=='1' else '0'*pick, temp) + data[pick]
        pick += 1

    temp = xor(key if temp[0]=='1' else '0'*pick, temp)
    return temp    

data = "1100110011100011"
key  = "1100000001111" 

codeword = data + divide(data + "0"*(len(key)-1), key)
print("Codeword with CRC:", codeword)






#dijkistra
import sys
def dijkstra(graph, start):
    dist = {n: sys.maxsize for n in graph}
    dist[start] = 0
    used = set()

    while len(used) < len(graph):
        u = min((n for n in graph if n not in used), key=lambda x: dist[x])
        used.add(u)

        for v, w in graph[u].items():
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


graph = {
    'A': {'B': 4, 'C': 1},
    'B': {'D': 1},
    'C': {'B': 2, 'D': 5},
    'D': {}
}

print("Shortest distances:", dijkstra(graph, 'A'))

