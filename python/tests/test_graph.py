from graph.graph import Graph

# - Node can be successfully added to the graph
def test_graph():
  graph = Graph()
  assert graph.add_node() == None

# - An edge can be successfully added to the graph

# - A collection of all nodes can be properly retrieved from the graph

# - All appropriate neighbors can be retrieved from the graph

# - Neighbors are returned with the weight between nodes included

# - The proper size is returned, representing the number of nodes in the graph

# - A graph with only one node and edge can be properly returned

# - An empty graph properly returns None

# - Ensure your tests are passing before you submit your solution.
