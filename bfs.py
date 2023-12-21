# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 05:22:34 2023

@author: arpud
"""

def bfs(start, adjacency_list):
    visited = set()
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        x = queue.pop(0)  

        for y in adjacency_list[x]:
            if y not in visited:
                visited.add(y)
                queue.append(y)
                
                T.append((x, y))


adjacency_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

T = []  

bfs('A', adjacency_list)


print("Edges in BFS tree:", T)
