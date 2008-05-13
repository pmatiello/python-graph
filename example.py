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
gr.add_nodes(["Atlantis","Wonderland","Brazil","Lemuria","Ys"])
gr.add_edge("Portugal", "Spain", wt=1)
gr.add_edge("Spain","France", wt=3)
gr.add_edge("France","Belgium", wt=2)
gr.add_edge("France","Germany", wt=3)
gr.add_edge("France","Italy", wt=3)
gr.add_edge("Belgium","Netherlands", wt=1)
gr.add_edge("Germany","Belgium", wt=2)
gr.add_edge("Germany","Netherlands", wt=2)
gr.add_edge("Germany","Italy", wt=3)
gr.add_edge("England","Wales", wt=1)
gr.add_edge("England","Scotland", wt=2)
gr.add_edge("Scotland","Wales", wt=1)

gr.add_edge("Atlantis","Wonderland")
gr.add_arrow("Atlantis","Brazil")
gr.add_edge("Atlantis","Lemuria")
gr.add_arrow("Lemuria","Ys")
gr.add_arrow("Ys","Wonderland")
gr.add_arrow("Ys","Brazil")

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
