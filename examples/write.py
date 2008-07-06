#!/usr/bin/env python

# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)

import sys
sys.path.append('..')
import graph

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

# print to XML
print gr.write()
