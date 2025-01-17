from main.Graph import Graph

g = Graph(adjacency_list={
    "a": ["b", "c"],
    "b": ["c"],
    "c": []
})

g.delete_edge("a", "b", directed=True)
print(g.adjacency_list)  # {'a': ['c'], 'b': ['c'], 'c': []}
