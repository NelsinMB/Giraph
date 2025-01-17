from main.Vertex import Vertex
from main.Edge import Edge
class Graph:

    def __init__(self, adjacency_list = {}, name = ""):
        self.name = name
        self.adjacency_list = adjacency_list.copy() if adjacency_list else {}

    def add_vertex(self, vertex_name):
        if vertex_name not in self.adjacency_list:
            self.adjacency_list[vertex_name] = []

    def delete_vertex(self, vertex):
        self.adjacency_list.pop(vertex_name, None)
        for neighbours in self.adjacency_list.values():
            if vertex_name in neighbours:
                neighbours.remove(vertex_name)

    def add_edge(self, from_vertex, to_vertex, undirected = False):
        self.adjacency_list[from_vertex].append(to_vertex)
        if undirected:
            self.adjacency_list[to_vertex].append(from_vertex)

    def delete_edge(self, from_vertex: str, to_vertex: str, directed: bool = False):
        """
        Deletes an edge between from_vertex and to_vertex
        - If directed=True, removes edge from_vertex to to_vertex only.
        - If directed=False, removes the edge in both directions (from_vertex to to_vertex and vice versa).

        Args:
            from_vertex (str): The starting vertex of the edge.
            to_vertex (str): The ending vertex of the edge.
            directed (bool): Whether the graph is directed. Default is False.
        """

        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].remove(to_vertex)
        else:
            print(f"Edge ({from_vertex}, {to_vertex}) does not exist.")

        if not directed:
            if to_vertex in self.adjacency_list and from_vertex in self.adjacency_list[to_vertex]:
                self.adjacency_list[to_vertex].remove(from_vertex)
            else:
                print(f"Edge ({to_vertex}, {from_vertex}) does not exist.")

    






