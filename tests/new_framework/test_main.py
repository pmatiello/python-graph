import unittest
import itertools

from pygraph.classes.Graph import graph
from pygraph.classes.Digraph import digraph

from test_directed import test_directed
from test_undirected import test_undirected
from test_common import test_common

GRAPH_NODES = { "trivial":1,
                "tiny":10,
                "big":100,
                #"huge":500 
                }

GRAPH_EDGES = GRAPH_NODES

GRAPH_TYPES = { "graph":( graph, ( test_undirected, test_common )),
                "digraph": (digraph, ( test_directed, test_common )), }

suite = unittest.TestSuite()

for size_name, order in GRAPH_NODES.iteritems():
    for edge_size_name, edge_count in GRAPH_EDGES.iteritems():
        for test_family, (test_class, base_classes) in GRAPH_TYPES.iteritems():
            complete_bases = tuple( itertools.chain( base_classes ,[unittest.TestCase, ] ) )
            
            test_name = "test_o_%s_e_%s_%s" % ( size_name, edge_size_name, test_family )
            
            class_members = { "test_class":test_class,
                              "graph_order":order,
                              "edge_count":edge_count, }
            
            new_test_class = type( test_name,  complete_bases, class_members, )
            globals()[test_name] = new_test_class
            
            
            suite.addTests( unittest.TestLoader().loadTestsFromTestCase( new_test_class ) )
            
            del new_test_class
        
if __name__ == "__main__":
    tr = unittest.TextTestRunner()
    result = tr.run( suite )
    print repr(result)
        
