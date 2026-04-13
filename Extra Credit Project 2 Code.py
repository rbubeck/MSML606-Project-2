# MSML 606 Extra Credit Project 2 Code: Single-Pair Shortest Path Problem using Dijkstra's Algorithm

import pandas as pd
import heapq

cities_df = pd.read_csv('Cities Graph Dataset.csv')

# Pick origin and destination cities
origin_city = input('Select an origin city (City#): ')
destination_city = input('Select an destination city (City#): ')

# Get all unique cities from the DataFrame
all_cities = pd.concat([cities_df['From'], cities_df['To']]).unique()

if origin_city not in all_cities or destination_city not in all_cities:
    print("Error: Invalid City")

else:

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

            for neighbor, weight in graph.get(current_node,[]):
                distance = current_dist + weight
                if distance < dist.get(neighbor,float('inf')):
                    dist[neighbor] = distance
                    path[neighbor] = current_node
                    heapq.heappush(pq, (distance,neighbor))

        # Reconstruct path
        final_path = []
        node = destination
        if dist[destination] == float('inf'):
            return float('inf'), []
        while node is not None:
            final_path.append(node)
            node = path[node]
        final_path.reverse()

        return dist[destination], final_path

    distance, path = dijkstra(cities_df,origin_city,destination_city)
    if distance == float('inf'):
        print(f"No path found from {origin_city} to {destination_city}")
    else:
        print(f"Shortest Distance from {origin_city} to {destination_city}: {distance}")
        print(f"Path from {origin_city} to {destination_city}: {path}")