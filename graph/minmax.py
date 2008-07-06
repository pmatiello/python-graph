# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
#                         Rhys Ulerich <rhys.ulerich@gmail.com>
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
Minimization and maximization algorithms for python-graph.

@sort: minimal_spanning_tree, shortest_path, _first_unvisited, _lightest_arrow
"""


# Module metadata
__authors__ = "Pedro Matiello, Rhys Ulerich"
__license__ = "MIT"


# Minimal spanning tree

def minimal_spanning_tree(graph):
	"""
	Minimal spanning tree.

	@attention: Minimal spanning tree meaningful only for weighted graphs.

	@type  graph: graph
	@param graph: Graph.

	@rtype:  dictionary
	@return: Generated spanning tree.
	"""
	visited = []			# List for marking visited and non-visited nodes
	spanning_tree = {}		# MInimal Spanning tree

	# Initialization
	for each in graph.get_nodes():
		spanning_tree[each] = None
	root = 1
	
	# Algorithm loop
	while (root):
		larrow = _lightest_arrow(graph, visited)
		if (larrow == (-1, -1)):
			root = _first_unvisited(graph, visited)
			visited.append(root)
		else:
			spanning_tree[larrow[1]] = larrow[0]
			visited.append(larrow[1])

	return spanning_tree


def _first_unvisited(graph, visited):
	"""
	Return first unvisited node.
	
	@type  graph: graph
	@param graph: Graph.

	@type  visited: list
	@param visited: List of nodes.
	
	@rtype:  node
	@return: First unvisited node.
	"""
	for each in graph.get_nodes():
		if (not each in visited):
			return each
	return None


def _lightest_arrow(graph, visited):
	"""
	Return the lightest arrow in graph going from a visited node to an unvisited one.
	
	@type  graph: graph
	@param graph: Graph.

	@type  visited: list
	@param visited: List of nodes.

	@rtype:  tuple
	@return: Lightest arrow in graph going from a visited node to an unvisited one.
	"""
	lightest_arrow = (-1, -1)
	weight = -1
	for each in visited:
		for other in graph.get_node(each):
			if (not other in visited):
				w = graph.get_arrow_weight(each, other)
				if (w < weight or weight < 0):
					lightest_arrow = (each, other)
					weight = w
	return lightest_arrow


# Shortest Path
# Code donated by Rhys Ulerich

def shortest_path(graph, source):
	"""
	Return the shortest path distance between source and all other nodes using Dijkstra's algorithm.
	
	@attention: All weights must be nonnegative.

	@type  graph: graph
	@param graph: Graph.

	@type  source: node
	@param source: Node from which to start the search.

	@rtype:  tuple
	@return: A tuple containing two dictionaries, each keyed by target nodes.
		1. Shortest path spanning tree (each key points to previous node in the shortest path transversal).
		2. Shortest distance from given source to each target node.
	Inaccessible target nodes do not appear in either dictionary.
	"""
	# Initialization
	dist	 = { source: 0 }
	previous = {}
	q = graph.get_nodes()

	# Algorithm loop
	while q:
		# examine_min process performed using O(nodes) pass here.
		# May be improved using another examine_min data structure.
		# See http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/GraphAlgor/dijkstraAlgor.htm
		u = q[0]
		for node in q[1:]:
			if ((not dist.has_key(u)) 
				or (dist.has_key(node) and dist[node] < dist[u])):
				u = node
		q.remove(u)

		# Process reachable, remaining nodes from u
		if (dist.has_key(u)):
			for v in graph.get_node(u):
				if v in q:
					alt = dist[u] + graph.get_arrow_weight(u, v)
					if (not dist.has_key(v)) or (alt < dist[v]):
						dist[v] = alt
						previous[v] = u

	return previous, dist
