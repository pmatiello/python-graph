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

# Print to DOT Language
dot = gr.write(fmt='dot')

# Print graph as PNG image
gvv = gv.readstring(dot)
gv.layout(gvv,'neato')
gv.render(gvv,'png')
