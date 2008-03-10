#!/usr/bin/env python

# Copyright (c) 2007 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)

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

# Set arrow and edge weights
print "Set edge and arrows weights"
g.set_arrow_weight(0, 1, 5)
g.set_edge_weight(0, 3, 12)
print g.weights

# Remove edges and arrows
g.del_edge(0, 1)
g.del_arrow(0,2)
print "Remove edges and arrows:", 
if (g.get_node(0) == [3] and g.get_node(2) == []): print "ok"
else: print "fail"

# Build graph for algorithms
g.add_edge(0, 2)
g.add_edge(2, 4)
g.add_edge(4, 1)
g.add_edge(3, 1)
g.add_edge(5, 6)
g.add_edge(5, 7)
print "Graph:", g

# Depht first search
print
print "Depth first search:"
print "i: ", range(0, len(g))
st, pre, post = g.depth_first_search()
print "st:", st
print "pre:", pre
print "post:", post

# Breadth first search
print
print "Breadth first search:"
print "i: ", range(0, len(g))
print "st:", g.breadth_first_search()

# Transitive closure
print
print "Transitive closure"
for each in g.accessibility():
	print each

# Strongly connected componets
print
print "Strongly connected components"
for each in g.mutual_accessibility():
	print each

# Topological sorting (not really valid here because g isn't directed nor acyclic)
print
print "Topological sorting"
print g.topological_sorting()

# Connected componets
print
print "Connected components"
print g.connected_components()
