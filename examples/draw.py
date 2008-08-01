#!/usr/bin/env python

# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)

import sys
sys.path.append('..')
sys.path.append('/usr/lib/graphviz/python/')
import graph
import gv

# Graph creation
gr = graph.graph()

# Add nodes and edges
gr.add_nodes(["Portugal","Spain","France","Germany","Belgium","Netherlands","Italy"])
gr.add_nodes(["England","Ireland","Scotland","Wales"])

gr.add_edge("Portugal", "Spain")
gr.add_edge("Spain","France")
gr.add_edge("France","Belgium")
gr.add_edge("France","Germany")
gr.add_edge("France","Italy",)
gr.add_edge("Belgium","Netherlands")
gr.add_edge("Germany","Belgium")
gr.add_edge("Germany","Netherlands")
gr.add_edge("England","Wales")
gr.add_edge("England","Scotland")
gr.add_edge("Scotland","Wales")

# Print to DOT Language
dot = gr.write(fmt='dot')

# Print graph as PNG image
gvv = gv.readstring(dot)
gv.layout(gvv,'neato')
gv.render(gvv,'png','graph.png')
