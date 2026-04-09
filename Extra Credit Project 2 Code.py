# MSML 606 Extra Credit Project 2 Code: Single-Pair Shortest Path Problem using Dijkstra's Algorithm

import pandas as pd
import heapq

cities_df = pd.read_csv('Cities Graph Dataset.csv')

# Pick origin and destination cities to calculate shortest path
origin_city = 'City1'
destination_city = 'City100'

# Dijkstra's Algorithm Function
def dijkstra(df,origin,destination):

    # Build graph from cities dataframe
    graph = {}

    for _, row in df.iterrows():
        u,v,w = row['From'],row['To'],row['Distance']
        graph.setdefault(u,[]).append((v,w))
        graph.setdefault(v,[]).append((u,w))

    # Priority Queue
    pq = [(0,origin)]

    # Distance Dictionary
    dist = {node: float('inf') for node in graph}
    dist[origin] = 0

    # Keep track of path
    path = {node: None for node in graph}

    while pq:

        current_dist, current_node = heapq.heappop(pq)

        if current_node == destination:
            break

        if current_dist > dist[current_node]:
            continue



    return

dijkstra(cities_df,origin_city,destination_city)