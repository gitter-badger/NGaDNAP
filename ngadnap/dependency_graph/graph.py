from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed

    def add_connection(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

class CommandGraph(Graph):
    """
        Graph data structure 
    """
    def __init__(self):
        super(CommandGraph, self).__init__(self,directed=True)
    
        

