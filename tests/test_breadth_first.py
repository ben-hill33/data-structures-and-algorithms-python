from breadth_first.breadth_first import BF_Graph

def breadth_first_graph():
  graph = BF_Graph()
  pandora = graph.add_node('Pandora')
  arendelle = graph.add_node('Arendelle')
  metroville = graph.add_node('Metroville')
  monstro = graph.add_node('Monstropolis')
  narnia = graph.add_node('Narnia')
  naboo = graph.add_node('Naboo')
  graph.add_edge(pandora, arendelle)
  graph.add_edge(arendelle, metroville)
  graph.add_edge(arendelle, monstro)
  graph.add_edge(metroville, narnia)
  graph.add_edge(metroville, naboo)
  graph.add_edge(monstro, naboo)
  graph.add_edge(narnia, naboo)
  return graph


def test_bsf():
  graph = breadth_first_graph()
  vertices = graph.get_nodes()
  expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstropolis', 'Narnia', 'Naboo']
  actual = graph.breadth_first(vertices[0])
  assert actual == expected

