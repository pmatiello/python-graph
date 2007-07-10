#!/usr/bin/env python

# Testing code

import graph

print "Tests"
# Graph creation
g = graph.graph()

# Add nodes
g.add_nodes(5)
g.add_nodes(3)
print "Add nodes:",
if (len(g) == 8): print "ok"
else: print "fail"

# Add edges and arrows
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_arrow(0,2)
print "Add edges and arrows:", 
if (g.get_node(0) == [1, 3, 2] and g.get_node(2) == []): print "ok"
else: print "fail"

# Remove edges and arrows
g.del_edge(0, 1)
g.del_arrow(0,2)
print "Remove edges and arrows:", 
if (g.get_node(0) == [3] and g.get_node(2) == []): print "ok"
else: print "fail"

g.depth_first_search()
