from collections import defaultdict

class graph(object):
        
    def __init__(self, arcList=[]):     
        
        self.arcs = defaultdict(list)

        for arc in arcList:
            self.arcs[arc[0]].append(arc[1])
            if not self.check_vertex(arc[1]):
                self.add_vertex(arc[1])
            
    def check_vertex(self,v):
        return v in self.arcs
        
    def check_arc(self,v,a):
        return a in self.arcs[v]
            
    def add_vertex(self,v):
        self.arcs[v]=[]
        
    def add_arc(self,v,a):
        self.arcs[v].append(a)
        
    def remove_vertex(self,v):
        self.arcs.pop(v,None)
        
    def remove_arc(self,v,a):
        self.arcs[v].remove(a)
        
    def get_arcs(self,v):
        return self.arcs[v]
            
        
