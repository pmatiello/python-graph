
class python_graph_exception( RuntimeError ):
    """
    A base-class for the various kinds of errors that occur in the the python-graph class.
    """
    
class unreachable( python_graph_exception ):
    """
    Goal could not be reached from start.
    """
    def __init__( self, start, goal ):
        msg = "Node %s could not be reached from node %s" % ( repr(goal), repr(start) )
        python_graph_exception.__init__( self, msg )
        self.start = start
        self.goal = goal