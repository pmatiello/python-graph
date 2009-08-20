#!/usr/bin/env python

# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
# License: MIT (see COPYING file)

import sys
sys.path.append('..')
sys.path.append('/usr/lib/graphviz/python/')
sys.path.append('/usr/lib64/graphviz/python/')
from pygraph.classes.hypergraph import hypergraph
from pygraph.readwrite.dot import write_hypergraph
import gv

# Graph creation
hgr = hypergraph()

# Add nodes and edges
hgr.add_nodes([1,2,3,4,5,6,7,8,9])
hgr.add_hyperedges(['A','B','C','J'])
hgr.link(1,'A')
hgr.link(2,'A')
hgr.link(3,'A')
hgr.link(4,'A')
hgr.link(4,'B')
hgr.link(5,'B')
hgr.link(6,'B')
hgr.link(7,'C')
hgr.link(8,'C')
hgr.link(9,'C')
hgr.link(1,'J')
hgr.link(2,'J')
hgr.link(3,'J')
hgr.link(4,'J')

# Print graph as PNG image
dot = write_hypergraph(hgr, colored=True)
gvv = gv.readstring(dot)
gv.layout(gvv,'neato')
gv.render(gvv,'png','hypergraph.png')
