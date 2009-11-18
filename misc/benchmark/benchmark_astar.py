import logging
import datetime

from pygraph.classes.digraph import digraph
from pygraph.classes.dict_digraph import dict_digraph
from random import randint, choice, shuffle, sample
from pygraph.algorithms.heuristics.chow import chow
from pygraph.algorithms.minmax import heuristic_search

log = logging.getLogger(__name__)

class benchmark_astar( object ):
    NUMBER_OF_ITERATIONS = 10
    GRAPH_ORDER = 500
    GRAPH_EDGES = GRAPH_ORDER * 10
    CHOW_REFERENCE_POINTS = 15
    NUMBER_OF_SEARCHES = 10
    
    @staticmethod
    def generate(random_graph, num_nodes, num_edges, weight_range=(0, 1) ):
        """
        Create a random graph.
        
        @type  num_nodes: number
        @param num_nodes: Number of nodes.
        
        @type  num_edges: number
        @param num_edges: Number of edges.
        
        @type  directed: bool
        @param directed: Whether the generated graph should be directed or not.  
    
        @type  weight_range: tuple
        @param weight_range: tuple of two integers as lower and upper limits on randomly generated
        weights (uniform distribution).
        """
        # Nodes
        nodes = range(num_nodes)
        random_graph.add_nodes(nodes)
        
        # Build a list of all possible edges
        edges = []
        edges_append = edges.append
        for x in nodes:
            for y in nodes:
                if ((random_graph.is_directed() and x != y) or (x > y)):
                    edges_append((x, y))
        
        # Shuffle the list of all possible edges
        for i in range(len(edges)):
            r = randint(0, len(edges)-1)
            edges[i], edges[r] = edges[r], edges[i]
        
            # Add edges to the graph
            min_wt = min(weight_range)
            max_wt = max(weight_range)
        for i in range(len(edges)):
            each = edges[i]
            random_graph.add_edge((each[0], each[1]), wt = randint(min_wt, max_wt))
    
        return random_graph
    
    
    def __init__(self, fn_create, test_name="xxx" ):
        self.fn_create = fn_create
        self.test_name = test_name
        self.test_times = []
    
    def __call__(self):
        for iteration in range(self.NUMBER_OF_ITERATIONS):
            log.warn("Test %i" % iteration)
            
            self.time_operation( self.run_benchmark )
        
        test_time = sum( self.test_times ) / len( self.test_times )
        
        log.warn("Average test time for %s is %.2f" % (self.test_name, test_time) )
            
    def time_operation(self, fn, *args, **kwargs ):
        """
        Time something
        """
        st = datetime.datetime.now()
        result = fn(*args, **kwargs)
        et = datetime.datetime.now()
        td = et - st
        seconds = td.microseconds / 1000000.0 + td.seconds + td.days * 86400
        
        self.test_times.append( seconds )
        
        return result
            
    def run_benchmark(self):
        G = self.fn_create()
        self.generate(G, self.GRAPH_ORDER, self.GRAPH_EDGES)
        
        reference_nodes = sample( G.nodes(), self.CHOW_REFERENCE_POINTS )
        heuristic = chow( *reference_nodes )
        heuristic.optimize(G)
        
        source_nodes = sample( G.nodes(), self.NUMBER_OF_SEARCHES )
        dest_nodes = sample( G.nodes(), self.NUMBER_OF_SEARCHES )
        
        for s,d in zip( source_nodes, dest_nodes ):
            log.warn("Searching from %s to %s" % (s,d) )
            result = heuristic_search( G, s, d, heuristic )
            
def fn_create_digraph():
    return digraph()

def fn_create_dict_digraph():
    return dict_digraph({})

if __name__ == "__main__":
    logging.basicConfig()
    
    benchmark_astar( fn_create_digraph, "digraph" )()
    benchmark_astar( fn_create_dict_digraph, "dict-digraph" )()
