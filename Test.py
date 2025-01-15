from main.Graph import Graph

x = Graph({'a': ['b', 'c'], 'b': ['c']}, "test")
print(x.adjacency_list.get('a'))
