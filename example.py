#!/usr/bin/env python

import graph

g = graph.graph()
g.add_nodes(5)
print "Size:", g.get_size()
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_arrow(0,2)
print g.get_node(0)
print g.get_node(2)
