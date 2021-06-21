from graph.graph import Graph, Vertex, Edge


def test_add_node():
  graph = Graph()
  expected = 'a'
  actual = graph.add_node('a').value
  assert expected == actual

def test_add_vertex_pass():
  vertex = Vertex("a")
  actual = vertex.value
  expected = "a"
  assert actual == expected

def test_add_vertex_fail():
  vertex = Vertex("a")
  actual = vertex.value
  expected = "b"
  assert actual != expected


def test_add_edge_true():
  graph = Graph()
  a = graph.add_node('a')
  b = graph.add_node('b')
  graph.add_edge(a, b)
  assert True


def test_get_all_nodes():
  graph = Graph()
  node = graph.add_node('node')
  node_two = graph.add_node('node_two')
  assert len(graph.get_nodes()) == 2


def test_graph_gets_neighbors():
  graph = Graph()
  node = graph.add_node('node')
  node_two = graph.add_node('node_two')
  graph.add_edge(node, node_two)
  neighbor = graph.get_neighbor(node)
  neighbor_two = neighbor[0]
  assert neighbor_two.vertex.value == 'node_two'
  assert len(neighbor) == 1

# - Neighbors are returned with the weight between nodes included
def test_graph_gets_neighbors():
  graph = Graph()
  node = graph.add_node('node')
  node_two = graph.add_node('node_two')
  graph.add_edge(node, node_two)
  neighbor = graph.get_neighbor(node)
  neighbor_two = neighbor[0]
  assert neighbor_two.vertex.value == 'node_two'
  assert len(neighbor) == 1
  assert neighbor_two.weight == 1


def test_size():
  graph = Graph()
  a = graph.add_node('a')
  b = graph.add_node('b')
  expected = 2
  actual = graph.size()
  assert actual == expected


def test_empty_graph_returns_none():
  graph = Graph()
  expected = None
  actual = graph.get_vertices([0])
  assert expected == actual
