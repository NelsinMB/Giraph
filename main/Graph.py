from main.Vertex import Vertex
from main.Edge import Edge
class Graph:

    def __init__(self, adjacency_list = {}, name = ""):
        self.name = name
        self.adjacency_list = adjacency_list
        self.vertex_set = []
        self.edge_set = []
        if adjacency_list: 
            self.construct_vertex_set(self.adjacency_list)
            self.construct_edge_set(self.adjacency_list)

    def construct_vertex_set(self, adjacency_list):
        vertex_set = []
        for k in adjacency_list:
            new_vertex = Vertex(k)
            self.vertex_set.append(new_vertex)


    def construct_edge_set(self, adjacency_list):
        for k,v in adjacency_list.items():
            for node in v:
                new_edge = Edge(self.find_vertex_with_name(k), self.find_vertex_with_name(node))
                self.edge_set.append(new_edge)

    def add_vertex(self):
        if vertex_name not in self.adjacency_list:
            new_vertex = Vertex(vertex_name)
            self.vertex_set.append(new_vertex)
            self.adjacency_list[vertex_name] = []
        else:
            print(f"Vertex {vertex_name} already exists.")

    def delete_vertex(self, vertex):
        self.vertex_set = [v for v in self.vertex_set if v.name != vertex.name] 
        self.adjacency_list.pop(vertex_name, None)
        for neighbours in self.adjacency_list.values():
            if vertex_name in neighbours:
                neighbours.remove(vertex_name)

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list:
            self.adjacency_list[from_vertex].append(to_vertex)
            new_edge = Edge(self.find_vertex_with_name(from_vertex), self.find_vertex_with_name(to_vertex))
            self.edge_set.append(new_edge)
        else: 
            print("One or both vertices not found.")

    def delete_edge(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list:
            self.adjacency_list[from_vertex].remove(to_vertex)
            self.edge_set = [e for e in self.edge_set if not (e.head.name == from_vertex and e.end.name == to_vertex)]


    def find_vertex_with_name(self, name: str) -> Vertex:
        for vertex in self.vertex_set:
            if vertex.name == name:
                return vertex
        return None
    






