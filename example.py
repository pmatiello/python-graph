#!/usr/bin/env python

# Copyright (c) 2007 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)

import graph

print "Example"
# Graph creation
gr = graph.graph()

# Add nodes and edges
gr.add_nodes(["Portugal","Spain","France","Germany","Belgium","Netherlands","Italy"])
gr.add_nodes(["England","Ireland","Scotland","Wales"])
gr.add_edge("Portugal", "Spain")
gr.add_edge("Spain","France")
gr.add_edge("France","Belgium")
gr.add_edge("France","Germany")
gr.add_edge("France","Italy")
gr.add_edge("Belgium","Netherlands")
gr.add_edge("Germany","Belgium")
gr.add_edge("Germany","Netherlands")
gr.add_edge("Germany","Italy")
gr.add_edge("England","Wales")
gr.add_edge("England","Scotland")
gr.add_edge("Scotland","Wales")

print "------------------------------------------------------------------------"
print "Simple printing"
print gr

print "------------------------------------------------------------------------"
print "Depth First Search"
print gr.depth_first_search()

print "------------------------------------------------------------------------"
print "Breadth First Search"
print gr.breadth_first_search()

print "------------------------------------------------------------------------"
print "Accessibility"
print gr.accessibility()

print "------------------------------------------------------------------------"
print "Mutual Accessibility"
print gr.mutual_accessibility()

print "------------------------------------------------------------------------"
print "Connected components"
print gr.connected_components()

print "------------------------------------------------------------------------"
print "Topological sorting"
print gr.topological_sorting()

print "------------------------------------------------------------------------"
print "Minimal Spanning Tree"
print gr.minimal_spanning_tree()
