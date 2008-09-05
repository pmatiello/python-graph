#!/usr/bin/python -u

# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.


"""
python-graph

This file contains tests for many python graph algorithms and operations.
"""


# Imports
import sys
sys.path.append('..')
import graph


# Now work
print "python-graph test suite"
gr = graph.graph()
yes = 0
no = 0
print "------------------------------------"


# Crash test
print
print "Crash test"

# Generate random graph
try:
	print "   Generating random graph...",
	gr.generate(200, 3000, directed=False, weight_range=(1,10))
	print "ok"
	yes = yes + 1
except:
	print "failed"
	no = no + 1

# Write graph to file
f = file('testgraph.xml','w')
f.write(gr.write())
f.close()

# Accessibility
try:
	print "   Accessibility...",
	gr.accessibility()
	print "ok"
	yes = yes + 1
except:
	print "failed"
	no = no + 1

# Breadth-first search
try:
	print "   Breadth-first search...",
	gr.breadth_first_search()
	print "ok"
	yes = yes + 1
except:
	print "failed"
	no = no + 1

# Connected components
try:
	print "   Connected components...",
	gr.connected_components
	print "ok"
	yes = yes + 1
except:
	print "failed"
	no = no + 1

# Cut-edges
try:
	print "   Cut-edges...",
	gr.cut_edges()
	print "ok"
	yes = yes + 1
except:
	print "failed"
	no = no + 1

# Cut-nodes
try:
	print "   Cut-nodes...",
	gr.cut_nodes()
	print "ok"
	yes = yes + 1
except:
	print "failed"
	no = no + 1	

# Depth-first search
try:
	print "   Depth-first search...",
	gr.depth_first_search()
	print "ok"
	yes = yes + 1
except:
	print "   failed"

# Minimal spanning tree
try:
	print "   Minimal spanning tree...",
	gr.minimal_spanning_tree()
	print "ok"
	yes = yes + 1
except:
	print "failed"
	no = no + 1

# Mutual-accessibility
try:
	print "   Mutual-accessibility...",
	gr.mutual_accessibility()
	print "ok"
	yes = yes + 1
except:
	print "failed"
	no = no + 1

# Shortest path
try:
	print "   Shortest path...",
	gr.shortest_path(0)
	print "ok"
	yes = yes + 1
except:
	print "   failed"

# Topological sorting
try:
	print "   Topological sorting...",
	gr.topological_sorting()
	print "ok"
	yes = yes + 1
except:
	print "failed"
	no = no + 1

# Correctness tests
print
print "Correctness tests"

# Connectivity (compared)
try:
	print "   Connectivity...",
	access = gr.accessibility()[0]
	bfs = gr.breadth_first_search(root=0)[0].keys()
	dfs = gr.depth_first_search(root=0)[0].keys()
	mst = gr.minimal_spanning_tree(root=0).keys()
	short = gr.shortest_path(0)[0].keys()
	access.sort()
	bfs.sort()
	dfs.sort()
	mst.sort()
	short.sort()
	if (access == dfs and dfs == bfs and bfs == mst and mst == short):
		print "ok"
		yes = yes + 1
	else:
		print "failed"
		no = no + 1
except:
	print "failed"
	no = no + 1

# Cut-edges
try:
	print "   Cut-edges...",
	grc = graph.graph()
	grc.generate(50,100)
	cuts = grc.cut_edges()
	max1 = 0
	pairing = grc.connected_components()
	for each in pairing.keys():
		if (pairing[each] > max1):
			max1 = pairing[each]
	if (len(cuts)):
		grc.del_edge(cuts[0][0], cuts[0][1])
		max2 = 0
		pairing = grc.connected_components()
		for each in pairing.keys():
			if (pairing[each] > max2):
				max2 = pairing[each]
		if (max1 != max2):
			print "ok"
			yes = yes + 1
		else:
			print "failed"
			no = no + 1
	else:
		print "could not check"
except:
	print "failed"
	no = no + 1

# Cut-nodes
try:
	print "   Cut-nodes...",
	grc = graph.graph()
	grc.generate(50,100)
	cuts = grc.cut_nodes()
	max1 = 0
	pairing = grc.connected_components()
	for each in pairing.keys():
		if (pairing[each] > max1):
			max1 = pairing[each]
	if (len(cuts)):
		for each in grc.get_edges():
			if (each[1] == cuts[0]):
				grc.del_edge(each[0],each[1])
		del(grc.nodes[cuts[0]])
		max2 = 0
		pairing = grc.connected_components()
		for each in pairing.keys():
			if (pairing[each] > max2):
				max2 = pairing[each]
		if (max1 != max2):
			print "ok"
			yes = yes + 1
		else:
			print "failed"
			no = no + 1
	else:
		print "could not check"
except:
	print "failed"
	no = no + 1


# Summary
print
print yes+no, "tests were made.",
print yes, "were successful,",
print no, "failed."
