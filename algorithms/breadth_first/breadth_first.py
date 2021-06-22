from data_structures.stacks_and_queues.stacks_and_queues import Queue
from data_structures.graph.graph import Graph


class BF_Graph(Graph):

    def breadth_first(self, vertex):
        node = []
        breadth = Queue()

        breadth.enqueue(vertex)
        visited = set()

        while not breadth.is_empty():
            front = breadth.dequeue()
            node.append(front.value)

            for neighbor in self.get_neighbor(front):
                if neighbor.vertex.value not in visited:
                    visited.add(neighbor.vertex.value)
                    breadth.enqueue(neighbor.vertex)
        return node
