# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)


import graph

#demo of the critical path algorithm and the transitivity detection algorithm

G = graph.digraph()

G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')

G.add_edge('A','B',1)
G.add_edge('A','C',2)
G.add_edge('B','C',10)
G.add_edge('B','D',2)
G.add_edge('B','E',8)
G.add_edge('C','D',7)
G.add_edge('C','E',3)
G.add_edge('E','D',1)
G.add_edge('D','F',3)
G.add_edge('E','F',1)
#add this edge to add a cycle
#G.add_edge('E','A',1)

print G.transitive_edges()
print G.critical_path()