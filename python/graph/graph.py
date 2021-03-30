
class Graph:
  def __init__(self):
    # will hold all the vertexes in graph
    self._adjacency_list = {}

  def add_node(self, value):
    vertex = Vertex(value)
    self._adjacency_list[vertex] = []
    return vertex
  
  def add_edge(self, start_vertex, end_vertex, weight=1):
    if start_vertex not in self._adjacency_list:
      raise KeyError('Start vertex not in graph')
    if end_vertex not in self._adjacency_list:
      raise KeyError('End of vertex')

    edge = Edge(end_vertex, weight)
    adjacencies = self._adjacency_list[start_vertex]
    adjacencies.append(edge)

  def get_nodes(self):
    return list(self._adjacency_list.keys())

  def get_neighbor(self, vertex):
    return self._adjacency_list.get(vertex, None)

  def size(self):
    return len(self._adjacency_list)

  def get_vertices(self, string):
    string_list = self.get_nodes()
    for i in range(len(string_list)):
      if string_list[i].value == string:
        return string_list[i]
    return None


class Vertex:
  def __init__(self, value):
    self.value = value

class Edge:
  def __init__(self, vertex, weight=1):
    self.vertex = vertex
    self.weight = weight

