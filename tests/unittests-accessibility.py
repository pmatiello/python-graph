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
Unittests for graph.algorithms.accessibility
"""


import unittest
import pygraph
import time

class test_find_cycle(unittest.TestCase):

    def setUp(self):
        pass

    def testDigraph(self):
        gr = pygraph.digraph()
        gr.add_nodes(xrange(25))
        edges = [(13, 22), (18, 0), (17, 8), (15, 13), (13, 19), (21, 2),
                 (3, 11), (11, 23), (4, 22), (4, 2), (3, 22), (23, 7), (12, 2),
                 (6, 7), (7, 15), (0, 15), (20, 21), (22, 16), (19, 14),
                 (22, 14), (7, 19), (0, 11), (9, 11), (12, 17), (15, 4),
                 (6, 15), (24, 10), (4, 10), (11, 4), (8, 2), (1, 23), (9, 22),
                 (10, 13), (5, 24), (4, 16), (23, 5), (6, 23), (11, 15), (22, 11),
                 (6, 12), (15, 14), (12, 22), (17, 4), (17, 9), (9, 13), (8, 3),
                 (21, 15), (24, 7), (1, 12), (4, 1), (11, 22), (0, 13), (18, 7),
                 (24, 3), (21, 10), (6, 13), (8, 22), (13, 9), (3, 4), (12, 8)]
        for each in edges:
            gr.add_edge(each[0], each[1])
        
        ma = gr.mutual_accessibility()
        for n in gr:
            for m in gr:
                if (m in ma[n]):
                    assert m in gr.depth_first_search(n)[0]
                    assert n in gr.depth_first_search(m)[0]
                else:
                    assert m not in gr.depth_first_search(n)[0] or n not in gr.depth_first_search(m)[0]