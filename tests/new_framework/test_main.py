import unittest
import itertools
import logging

from pygraph.classes.Graph import graph
from pygraph.classes.Digraph import digraph

from test_directed import test_directed
from test_undirected import test_undirected
from test_common import test_common

log = logging.getLogger( __name__ )

GRAPH_NODES = { "trivial":1,
                "really_small":2,
                "tiny":10,
                "big":100,
                "huge":250 
                }

GRAPH_EDGES = GRAPH_NODES

GRAPH_TYPES = { "graph":( graph, ( test_undirected, test_common )),
                "digraph": (digraph, ( test_directed, test_common )), }

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger("").setLevel( logging.INFO )

def valid_combo( nodes, edges ):
    """
    Exclude certain types of graph as they are too boring to test.
    """
    if nodes > 10:
        return True
    
    if edges < nodes:
        return True
    
    return False

suite = unittest.TestSuite()

for size_name, order in GRAPH_NODES.iteritems():
    for edge_size_name, edge_count in GRAPH_EDGES.iteritems():
        if valid_combo( order, edge_count ):    
            for test_family, (test_class, base_classes) in GRAPH_TYPES.iteritems():
                complete_bases = tuple( itertools.chain( base_classes ,[unittest.TestCase, ] ) )
                
                test_name = "test_o_%s_e_%s_%s" % ( size_name, edge_size_name, test_family )
                log.info("Generating test-case %s" % test_name)
                
                class_members = { "test_class":test_class,
                                  "graph_order":order,
                                  "edge_count":edge_count, }
                
                new_test_class = type( test_name,  complete_bases, class_members, )
                globals()[test_name] = new_test_class
                
                
                suite.addTests( unittest.TestLoader().loadTestsFromTestCase( new_test_class ) )
                
                del new_test_class
        
if __name__ == "__main__":
    
    tr = unittest.TextTestRunner( verbosity=2 )
    result = tr.run( suite )
    print repr(result)
        
