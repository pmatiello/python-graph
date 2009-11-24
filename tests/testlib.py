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
Helper functions for unit-tests.
"""


# Imports
from pygraph.algorithms.generators import generate, generate_hypergraph
from random import seed
from time import time
from sys import argv

# Configuration
random_seed = int(time())
num_nodes = { 'tiny': 10,
              'small': 25,
              'medium': 50,
              'big': 100
             } 
num_edges = { 'tiny': 18,
              'small': 120,
              'medium': 490,
              'big': 1980
             }
sizes = ['tiny', 'small', 'medium', 'big']
use_size = 'small'

# Init
try:
    if (argv[0] != 'testrunner.py'):
        print
        print ("Random seed: %s" % random_seed)
except:
    pass


def new_graph():
    seed(random_seed)
    return generate(num_nodes[use_size], num_edges[use_size])

def new_digraph():
    seed(random_seed)
    return generate(num_nodes[use_size], num_edges[use_size], directed=True)

def new_hypergraph():
    seed(random_seed)
    return generate_hypergraph(num_nodes[use_size], num_edges[use_size])

def new_uniform_hypergraph(_r):
    seed(random_seed)
    return generate_hypergraph(num_nodes[use_size], num_edges[use_size], r = _r)
