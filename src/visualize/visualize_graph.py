import networkx as nx 
import matplotlib.pyplot as plt 


class GraphVisualization:    
    def __init__(self): 
        self.visual = []
        self.options = {
            "node_color": "#A0CBE2",
            "width": 3,
            "edge_cmap": plt.cm.Blues,
            "font_size": 10
        }
          
    def add_edge(self, a, b, label): 
        temp = [a, b, label] 
        self.visual.append(temp) 
          
    def visualize(self): 
        G = nx.Graph() 
        edge_labels = {}
        for edge in self.visual:
            G.add_edge(edge[0], edge[1])
            edge_labels[(edge[0], edge[1])] = edge[2]
        
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, **self.options)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show() 
