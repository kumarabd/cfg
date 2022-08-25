import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self,cfg=None):
        self.graph = {}
        for ob in cfg:
            if ob.parent:
                if ob.parent in self.graph:
                    self.graph[ob.parent.value()].append(ob.value())
                else:
                    self.graph[ob.parent.value()] = [ob.value()]
                if ob.value() in self.graph:
                    self.graph[ob.value()].append(ob.parent.value())
                else:
                    self.graph[ob.value()] = [ob.parent.value()]

    def edges(self):
      edgename = []
      for vrtx in self.graph:
         for nxtvrtx in self.graph[vrtx]:
            if {nxtvrtx, vrtx} not in edgename:
               edgename.append({vrtx, nxtvrtx})
      return edgename

    def show(self):
        edges_list = []
        for val in self.edges():
            if len(list(val)) > 1:
                edges_list.append(list(val))
        print(edges_list)

        G = nx.Graph()
        G.add_edges_from(edges_list)
        nx.draw_networkx(G)
        plt.show()


