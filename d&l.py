#distance-vector
g = [
    [0,2,7],
    [2,0,1],
    [7,1,0]
]

V = 3
for src in range(V):
    dist = [999]*V
    dist[src] = 0

    for _ in range(V-1):
        for u in range(V):
            for v in range(V):
                if g[u][v] and dist[u] + g[u][v] < dist[v]:
                    dist[v] = dist[u] + g[u][v]

    print("From node", src, ":", dist)







#leaky-bucket
def leaky_bucket(bsize, orate, incoming):
    count = 0  

    for i in range(len(incoming)):
        total = incoming[i] + count     
        sent = min(total, orate)         
        remaining = total - sent         

        
        if remaining > bsize:
            drop = remaining - bsize
            remaining = bsize
        else:
            drop = 0

        count = remaining  

        
        print("Sec:", i+1, "In:", incoming[i], "Sent:", sent, 
              "Drop:", drop, "Remain:", remaining)


leaky_bucket(5, 3, [1, 2])
