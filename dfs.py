# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 05:32:39 2023

@author: arpud
"""

def dfs(v, adjacency_list, visited):
    visited.add(v)
    print("Visited:", v)

    for w in adjacency_list[v]:
        if w not in visited:
            dfs(w, adjacency_list, visited)

def dfs_all_vertices(vertices, adjacency_list):
    visited = set()

    for v in vertices:
        if v not in visited:
            dfs(v, adjacency_list, visited)

# Example usage
adjacency_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

vertices = list(adjacency_list.keys())

dfs_all_vertices(vertices, adjacency_list)
