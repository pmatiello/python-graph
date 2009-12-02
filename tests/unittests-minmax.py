# Copyright (c) Pedro Matiello <pmatiello@gmail.com>
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
Unittests for graph.algorithms.searching
"""


# Imports
import unittest
import testlib
from pygraph.classes.graph import graph
from pygraph.algorithms.searching import depth_first_search
from pygraph.algorithms.minmax import minimal_spanning_tree
from copy import deepcopy

def tree_weight(gr, tree):
    sum = 0;
    for each in tree:
        sum = sum + gr.edge_weight((each, tree[each]))
    return sum

def add_spanning_tree(gr, st):
    # A very tolerant implementation.
    gr.add_nodes(list(st.keys()))
    for each in st:
        if ((st[each] is not None) and (not gr.has_edge((st[each], each)))): # Accepts invalid STs
            gr.add_edge((st[each], each))

class test_spanning_tree(unittest.TestCase):

    def test_minimal_spanning_tree_on_graph(self):
        gr = testlib.new_graph(wt_range=(1,10))
        mst = minimal_spanning_tree(gr, root=0)
        wt = tree_weight(gr, mst)
        len_dfs = len(depth_first_search(gr, root=0)[0])
        for each in mst:
            if (mst[each] != None):
                mst_copy = deepcopy(mst)
                del(mst_copy[each])
                for other in gr[each]:
                     mst_copy[each] = other
                     if (tree_weight(gr, mst_copy) < wt):
                         gr2 = graph()
                         add_spanning_tree(gr2, mst_copy)
                         assert len(depth_first_search(gr2, root=0)[0]) < len_dfs
                                     
            
if __name__ == "__main__":
    unittest.main()