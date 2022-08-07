from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

    #constructor of the graph
    def __init__(self):
        self.Nodes= {}
        self.Edges= {}
        self.mc = 0

    def v_size(self) -> int:
        return self.Nodes.__len__()

    def e_size(self) -> int:
        sum=0
        for key, v in self.Edges.items():
            sum = sum + len(v)
        return sum

    # returns counter changes of the graph
    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
         if id1 in self.Nodes.keys() and id2 in self.Nodes.keys():
            self.Edges[id1][id2]=weight
            self.mc = self.mc + 1
            return True
         else: return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
            self.Nodes[node_id]=Node(node_id,pos)
            self.Edges[node_id]={}
            self.mc=self.mc+1
            return True

    def remove_node(self, node_id: int) -> bool:
        if self.Nodes[node_id]!=None:
            del self.Nodes[node_id]
            del self.Edges[node_id]
            listToRemove=[]
            for src, dest in self.Edges.items():
                for key in dest.keys():
                    if key==node_id:
                        listToRemove.append((src,key))

            for t in listToRemove:
                self.remove_edge(t[0],t[1])

            self.mc = self.mc + 1
            return True
        else: return False


    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.Edges[node_id1][node_id2]!=None:
            del self.Edges[node_id1][node_id2]
            self.mc = self.mc + 1
            return True
        else: return False

    def __str__(self):
        return f"Nodes:{self.Nodes}\nEdges:{self.Edges}"