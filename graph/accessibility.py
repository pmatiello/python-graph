# Copyright (c) 2007 Pedro Matiello <pmatiello@gmail.com>
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
Accessibility algorithms for python-graph.
"""


# Module metadata
__authors__ = "Pedro Matiello"
__license__ = "MIT"


# Imports
import graph


# Transitive-closure

def accessibility(graph):
	"""
	Accessibility matrix (transitive closure).

	@type  graph: graph
	@param graph: Graph.

	@rtype:  list
	@return: Accessibility matrix
	"""
	accessibility = []	# Accessibility matrix

	# For each node i, mark each node j so that exists a path from i to j.
	for i in graph.get_nodes():
		access = []
		for j in graph.get_nodes():
			access.append(0)
		_dfs(graph, access, 1, i)	# Perform DFS to explore all reachable nodes
		accessibility.append(access)
	return accessibility


# Strongly connected components

def mutual_accessibility(graph):
	"""
	Mutual-accessibility matrix (strongly connected components).

	@type  graph: graph
	@param graph: Graph.

	@rtype:  list
	@return: Mutual-accessibility matrix
	"""
	accessibility = graph.accessibility()	# Accessibility matrix (will become mutual-accessibility matrix)
	grsize = len(accessibility)

	# Given the accessibility matrix, verify the relation of mutual-accessibility.
	for i in xrange(grsize):
		for j in xrange(grsize - i):
			if (accessibility[i][i+j] != accessibility[i+j][i]):	# Verify if accessibility is not mutual
				accessibility[i][i+j] = 0
				accessibility[i+j][i] = 0
	return accessibility


# Connected components

def connected_components(graph):
	"""
	Connected components.

	@attention: Indentification of connected components is meaningful only for non-directed graphs.

	@type  graph: graph
	@param graph: Graph.

	@rtype:  list
	@return: List that associates each node to its connected component.
	"""
	visited = []
	count = 1

	# Initialization
	for each in graph.get_nodes():
		visited.append(0)

	# For 'each' node not found to belong to a connected component, find its connected component.
	for each in graph.get_nodes():
		if (not visited[each]):
			_dfs(graph, visited, count, each)
			count = count + 1
	
	return visited


# Limited DFS implementation used by algorithms here

def _dfs(graph, visited, count, node):
	"""
	Depht-first search subfunction adapted for accessibility algorithms.
	
	@type  graph: graph
	@param graph: Graph.

	@type  visited: list
	@param visited: List of nodes (visited nodes are marked non-zero).

	@type  node: number
	@param node: Node to be explored by DFS.
	"""
	visited[node] = count
	# Explore recursively the connected component
	for each in graph.get_node(node):
		if (not visited[each]):
			_dfs(graph, visited, count, each)

