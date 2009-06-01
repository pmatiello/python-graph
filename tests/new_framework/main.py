import unittest

from pygraph.classes import Graph
from pygraph.classes import Digraph

GRAPH_SIZES = { "trivial":1,
                "tiny":10,
                "big":100,
                "huge":1000 }

GRAPH_TYPES = { "graph":( Graph,  ) }

for size_name, order in GRAPH_SIZES:
    