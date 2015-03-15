
---

![http://dl.dropbox.com/u/1823095/python-graph/logo.png](http://dl.dropbox.com/u/1823095/python-graph/logo.png)


---


**python-graph** is a library for working with graphs in Python.

This software provides ﻿a suitable data structure for representing graphs and a whole set of important algorithms.

The code is appropriately documented and API reference is generated automatically by [epydoc](http://epydoc.sourceforge.net/).

Comments, bug reports and suggestions are welcome.


---

**Current release:** 1.8.2 - Jul 14, 2012

Please check our [Changelog](Changelog.md) for detailed information.

---

**Installing**

If you have `easy_install` on your system, you can simply run:

|`# easy_install python-graph-core`|
|:---------------------------------|

And, optionally, for Dot-Language support:

|`# easy_install python-graph-dot`|
|:--------------------------------|

Otherwise, you can download a package from the [Downloads](http://code.google.com/p/python-graph/downloads/list) page.

**Dependencies**: The Core module requires Python 2.6 or 3.x. Dot-Language support requires Python 2.6, `pydot` and `pyparsing`.

---


**Provided features and algorithms:**

  * Support for directed, undirected, weighted and non-weighted graphs
  * Support for hypergraphs
  * Canonical operations
  * XML import and export
  * DOT-Language import and export (for usage with [Graphviz](http://www.graphviz.org/))
  * Random graph generation

  * Accessibility (transitive closure)
  * Breadth-first search
  * Critical path algorithm
  * Cut-vertex and cut-edge identification
  * Cycle detection
  * Depth-first search
  * Gomory-Hu cut-tree algorithm
  * Heuristic search (A`*` algorithm)
  * Identification of connected components
  * Maximum-flow / Minimum-cut (Edmonds-Karp algorithm)
  * Minimum spanning tree (Prim's algorithm)
  * Mutual-accessibility (strongly connected components)
  * Pagerank algorithm
  * Shortest path search (Dijkstra's algorithm)
  * Shortest path search (Bellman-Ford algorithm)
  * Topological sorting
  * Transitive edge identification