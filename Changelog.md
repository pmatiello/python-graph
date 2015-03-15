### Release 1.8.2 ###
Jul 14, 2012

**Fixes:**
  * The find\_cycle function now accepts instances of any subtype of graph and digraph.

### Release 1.8.1 ###
Jan 08, 2012

**Enhancements:**
  * Shortest-path now executes in O(n\*log(n)) instead of O(n^2).

**Fixes:**
  * Shortest-path raises KeyError when the source node is not on the graph;
  * Bellman-Ford algorithm now works for unconnected graphs ([Issue 87](https://code.google.com/p/python-graph/issues/detail?id=87));
  * Linking, unlinking and relinking a hypernode to hyperedge now works as expected ([Issue 86](https://code.google.com/p/python-graph/issues/detail?id=86));
  * Graph comparison does not raise exceptions anymore ([Issue 88](https://code.google.com/p/python-graph/issues/detail?id=88));
  * Fixed undesired sharing of attribute lists ([Issue 92](https://code.google.com/p/python-graph/issues/detail?id=92));
  * Fixed reading of XML-stored graphs with edge attributes;
  * Fixed calculation of minimal spanning trees of graphs with negative-weighted edges ([Issue 102](https://code.google.com/p/python-graph/issues/detail?id=102)).

### Release 1.8.0 ###
Oct 01, 2010

**Enhancements:**
  * Added Pagerank algorithm;
  * Added Gomory-Hu cut-tree algorithm.

**Fixes:**
  * Edges from one node to itself are no longer duplicated ([Issue 75](https://code.google.com/p/python-graph/issues/detail?id=75)).

### Release 1.7.0 ###
Mar 20, 2010

**Enhancements:**
  * Added equality test for graphs, digraphs and hypergraphs;
  * Added has\_edge() and has\_hyperedge() methods to hypergraph objects;
  * Accepting subtypes of graph, digraph and hypergraph in dot-language output ([Issue 64](https://code.google.com/p/python-graph/issues/detail?id=64));
  * Added Bellman-Ford algorithm;
  * Added Edmonds-Karp Maximum-Flow algorithm.

**Fixes:**
  * Adding an edge with a label to a digraph now works again;
  * Deleting an edge of a hypergraph now deletes its attributes;
  * Node attributes on hypergraphs work now;
  * Checking for node equality correctly in find\_cycle;
  * Avoiding errors caused by deep recursion on many algorithms ([Issue 66](https://code.google.com/p/python-graph/issues/detail?id=66)).

### Release 1.6.3 ###
Dec 13, 2009

**Enhancements:**
  * Added Python3 support (support for Python 2.5 and lower was dropped).

**Fixes:**
  * Adding a graph to a digraph now works ([Issue 39](https://code.google.com/p/python-graph/issues/detail?id=39));
  * Fixed the reading of graphs and digraphs stored in XML.

**Important API Changes:**
  * Edges are now passed around as generic objects. In the case of graph / digraph this is a tuple.
  * Removed traversal() method from graph and digraph classes;
  * Removed accessibility, connected\_components, cut\_nodes and cut\_hyperedges from hypergraph class;
  * Functions for reading a hypergraph doesn't take an empty hypergraph as argument anymore.


### Release 1.6.2 ###
Sep 30, 2009

**Important API Changes:**
  * Adding an arrow to an non existing node on a digraph now fails sanely ([Issue 35](https://code.google.com/p/python-graph/issues/detail?id=35));
  * Adding an already added node to a graph or digraph now raises an exception;
  * Adding an already added edge to a graph or digraph now raises an exception;
  * pygraph.classes.Classname.classname classes were renamed to pygraph.classes.classname.classname;
  * pygraph.algorithms.filters.Filtername.filtername filters were renamed to pygraph.algorithms.filters.filtername.filtername;
  * pygraph.algorithms.heuristics.Heuristicname.heuristicname heuristics were renamed to pygraph.algorithms.heuristics.heuristicname.heuristicname;
  * hypergraph's read() and write() methods were removed.


### Release 1.6.1 ###
Jul 04, 2009

**Enhancements:**
  * Added reverse method to the digraph class.

**Important API Changes:**
  * Removed methods calling algorithms from graph and digraph classes;
  * pygraph.algorithms.cycles.find\_cycle does not take argument directed anymore;
  * Removed methods read, write and generate from graph and digraph classes;
  * Functions for writing and reading graphs now in pygraph algorithms.


### Release 1.6.0 ###
Jun 06, 2009

**Important API Changes:**
  * Module name was renamed to pygraph;
  * python\_graph\_exception was renamed to `GraphError`;
  * Exception unreachable was renamed to `NodeUnreachable`;
  * get\_edge\_weight was renamed to edge\_weight;
  * get\_edge\_label was renamed to edge\_label;
  * get\_edge\_attributes was renamed to edge\_attributes;
  * get\_node\_attributes was renamed to node\_attributes;
  * degree was renamed to node\_degree;
  * order was renamed to node\_order.

### Release 1.5.0 ###
May 03, 2009

**Enhancements:**
  * Assymptotically faster Mutual Accessibility (now using Tarjan's algorithm);
  * DOT-Language importing;
  * Transitive edge detection;
  * Critical path algorithm.

**Fixes:**
  * Cycle detection algorithm was reporting wrong results on some digraphs;
  * Removed Minimal Spanning Tree from Digraphs as Prim's algorithm does not work on them ([Issue 28](https://code.google.com/p/python-graph/issues/detail?id=28)).
  * Deletion of A--A edge raised an exception;
  * Deletion of an node with an A--A edge raised an exception.

**Important API Changes:**
  * Removed minimal\_spanning\_tree() method from the digraph class.


### Release 1.4.2 ###
Feb 22, 2009

**Fixes:**
  * find\_cycle() trapped itself in infinite recursion in some digraphs ([Issue 22](https://code.google.com/p/python-graph/issues/detail?id=22)).


### Release 1.4.1 ###
Feb 09, 2009

**Fixes:**
  * graph.algorithms.filters was not being installed ([Issue 20](https://code.google.com/p/python-graph/issues/detail?id=20)).


### Release 1.4.0 ###
Feb 07, 2009

**Enhancements:**
  * Added A`*` search algorithm (as heuristic\_search);
  * Added Chow's and Euclidean heuristics for A`*`;
  * Added filtered depth-first and breadth-first search;
  * Added 'find' search filter (stops the search after reaching a target node);
  * Added 'radius' search filter (radial limit for searching);
  * Moved to setuptools.

**Fixes:**
  * Breadth first search was omitting the first node in level ordering when no root was specified.


### Release 1.3.1 ###
Oct 27, 2008

**Fixes:**
  * Graph and digraph inverse was not working;
  * Node removal in digraphs was not deleting all relevant edges ([Issue 13](https://code.google.com/p/python-graph/issues/detail?id=13)).

**Important API Changes:**
  * Deprecated methods were removed.


### Release 1.3.0 ###
Sep 28, 2008

**Enhancements:**
  * Tree traversals (preorder and postorder).

**Fixes:**
  * Node insertion is much faster now ([Issue 11](https://code.google.com/p/python-graph/issues/detail?id=11)).
  * Hypernode/hyperedge insertion also much faster.

**Important API Changes:**
  * get\_nodes() is now nodes();
  * get\_edges() is now edges();
  * get\_neighbors() is now neighbors();
  * get\_incidents() is now incidents();
  * get\_order() is now order();
  * get\_degree() is now degree().
> (Former method names are deprecated and will be removed in the next release.)


### Release 1.2.0 ###
Sep 9, 2008

**Enhancements:**
  * Moved to new class style;
  * Graphs and digraphs are separated classes now;
  * Added level-based ordering to breadth first search;
  * Graph object is now iterable;
  * Graph object is now a container and graphobj`[`nodeid`]` iterates too;
  * Support for node and edge attributes ([Issue 5](https://code.google.com/p/python-graph/issues/detail?id=5));
  * Node deletion.

**Fixes:**
  * Install now works with a prefix ([Issue 10](https://code.google.com/p/python-graph/issues/detail?id=10));
  * Shortest path spanning trees did not had an explicit root.

**Important API Changes:**
  * breadth\_first\_search() now returns a tuple;
  * Arrow methods are gone. Use class digraph + edge methods for directed graphs now.


### Release 1.1.1 ###
Sep 4, 2008

**Enhancements:**
  * Improved install script.

**Fixes:**
  * DOT Language output now works for nodes/edges labelled with spaces.

**Important API Changes:**
  * get\_neighbours() is now get\_neighbors() ([Issue 9](https://code.google.com/p/python-graph/issues/detail?id=9)).


### Release 1.1.0 ###
Aug 31, 2008

**Enhancements:**
  * Hypergraph support ([Issue 4](https://code.google.com/p/python-graph/issues/detail?id=4));
  * Complete and complement graph generation;
  * Weights in random generated graphs ([Issue 8](https://code.google.com/p/python-graph/issues/detail?id=8)).

**Fixes:**
  * Fixed bug in cut-node identification;
  * Fixed bug causing wrong results for graphs with nodes labelled with values that evaluate to False ([Issue 7](https://code.google.com/p/python-graph/issues/detail?id=7)).

**Important API Changes:**
  * get\_edges() now return all edges in the graph;
  * get\_neighbours() has the former behaviour of get\_edges().


### Release 1.0.0 ###
Aug 01, 2008

  * Adds some operations;
  * Random graph generation;
  * Cut-vertex/cut-edge identification.


### Release 0.85 ###
Jul 27, 2008

  * Adds DOT-Language output ([Issue 1](https://code.google.com/p/python-graph/issues/detail?id=1));
  * Install script included ([Issue 3](https://code.google.com/p/python-graph/issues/detail?id=3)).


### Release 0.75 ###
Jul 06, 2008

  * Added XML import/export;
  * Docs are bundled now.


### Release 0.65 ###
Jun 25, 2008

  * DFS, BFS and MST can be generated for given roots;
  * Added Dijkstra's shortest path algorithm ([Issue 2](https://code.google.com/p/python-graph/issues/detail?id=2)).


### Release 0.50 ###
May 13, 2008

  * Some API changes;
  * Nodes can now be arbitrary names/objects.


### Release 0.45 ###
May 12, 2008

  * Adds Prim's minimal spanning tree.


### Release 0.40 ###
Mar 09, 2008

  * Adds topological sorting;
  * Support for weighted graphs.


### Release 0.30 ###
Aug 30, 2007

  * Adds algorithms for accessibility and mutual accessibility.

### Release 0.20 ###
Jul 16, 2007

  * Adds breadth-first search;
  * API documentation.


### Release 0.10 ###
Jul 10, 2007

  * First release;
  * Feat. basic operations and depth-first searching.