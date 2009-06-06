#!/usr/bin/env python

# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)

import sys
sys.path.append('..')
import pygraph
sys.path.append('/usr/lib/graphviz/python/')
sys.path.append('/usr/lib64/graphviz/python/')
import gv
from pygraph.algorithms.searching import breadth_first_search

# Graph creation
gr = pygraph.graph()

# Add nodes and edges
gr.add_nodes(["Portugal","Spain","France","Germany","Belgium","Netherlands","Italy"])
gr.add_nodes(["Switzerland","Austria","Denmark","Poland","Czech Republic","Slovakia","Hungary"])
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
gr.add_edge("Switzerland","Austria")
gr.add_edge("Switzerland","Germany")
gr.add_edge("Switzerland","France")
gr.add_edge("Switzerland","Italy")
gr.add_edge("Austria","Germany")
gr.add_edge("Austria","Italy")
gr.add_edge("Austria","Czech Republic")
gr.add_edge("Austria","Slovakia")
gr.add_edge("Austria","Hungary")
gr.add_edge("Denmark","Germany")
gr.add_edge("Poland","Czech Republic")
gr.add_edge("Poland","Slovakia")
gr.add_edge("Poland","Germany")
gr.add_edge("Czech Republic","Slovakia")
gr.add_edge("Czech Republic","Germany")
gr.add_edge("Slovakia","Hungary")

# Draw as PNG
dot = gr.write(fmt='dot')
gvv = gv.readstring(dot)
gv.layout(gvv,'dot')
gv.render(gvv,'png','europe.png')

# Then, draw the breadth first search spanning tree rooted in Switzerland
st, order = breadth_first_search(gr, root="Switzerland")
gst = pygraph.digraph()
gst.add_spanning_tree(st)

dot = gst.write(fmt='dot')
gvv = gv.readstring(dot)

gv.layout(gvv,'dot')
gv.render(gvv,'png','europe-st.png')

