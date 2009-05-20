# Copyright (c) 2007-2009 Pedro Matiello <pmatiello@gmail.com>
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

A library for working with graphs in Python.

@version: 1.6.0

Data structure classes are exposed at the top-level:
    - The L{graph} class is exposed as C{pygraph.graph()}.
    - The L{digraph} class is exposed as C{pygraph.digraph()}.
    - The L{hypergraph} class is exposed as C{pygraph.hypergraph()}.

Helper classes are exposed one level beneath:
    - L{Exceptions<pygraph.exceptions>} are exposed in C{pygraph.exceptions}.
    - L{Search filters<pygraph.filters>} are exposed in C{pygraph.filters}.
    - L{Heuristics<pygraph.heuristics>} for the A* algorithm are exposed in C{pygraph.heuristics}.

A quick introductory example:

>>> # Import the module and instantiate a graph object
>>> import graph
>>> gr = graph.graph()
>>> # Add nodes
>>> gr.add_nodes(['X','Y','Z'])
>>> gr.add_nodes(['A','B','C'])
>>> # Add edges
>>> gr.add_edge('X','Y')
>>> gr.add_edge('X','Z')
>>> gr.add_edge('A','B')
>>> gr.add_edge('A','C')
>>> gr.add_edge('Y','B')
>>> # Depth first search rooted on node X
>>> st, pre, post = gr.depth_first_search(root='X')
>>> # Print the spanning tree
>>> print st
{'A': 'B', 'C': 'A', 'B': 'Y', 'Y': 'X', 'X': None, 'Z': 'X'}
"""

# Imports
import pygraph.algorithms as algorithms
import pygraph.algorithms.filters as filters
import pygraph.algorithms.heuristics as heuristics
from pygraph.classes.Graph import graph
from pygraph.classes.Digraph import digraph
from pygraph.classes.Hypergraph import hypergraph
import pygraph.classes.Exceptions as exceptions
