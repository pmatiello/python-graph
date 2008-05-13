#!/usr/bin/env python

# Copyright (c) 2007 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)

import graph

print "Example"
# Graph creation
gr = graph.graph()

# Add nodes
gr.add_nodes(["Portugal","Spain","France","Germany","Belgium","Netherlands", "Italy"])
gr.add_edge("Portugal", "Spain")
gr.add_edge("Spain","France")
gr.add_edge("France","Belgium")
gr.add_edge("France","Germany")
gr.add_edge("France","Italy")
gr.add_edge("Belgium","Netherlands")
gr.add_edge("Germany","Belgium")
gr.add_edge("Germany","Netherlands")
gr.add_edge("Germany","Italy")

print "------------------------------------------------------------------------"
print "Simple printing"
print gr.get_nodes()
print gr.get_node("France")

print "------------------------------------------------------------------------"
print "Depth First Search"
print gr.depth_first_search()

print "------------------------------------------------------------------------"
print "Breadth First Search"
print gr.breadth_first_search()

print "------------------------------------------------------------------------"
