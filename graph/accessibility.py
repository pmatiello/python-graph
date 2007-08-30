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
import searching


# Transitive-closure
def accessibility(graph):
	"""
	Accessibility matrix (transitive closure).

	@type  graph: graph
	@param graph: Graph.

	@rtype:  list
	@return: Accessibility matrix
	"""
	accessibility = []

	for i in graph.get_nodes():
		access = []
		for j in graph.get_nodes():
			access.append(0)
		_dfs(graph, access, 1, i)
		accessibility.append(access)
	return accessibility


def mutual_accessibility(graph):
	"""
	Mutual-accessibility matrix (strongly connected components).

	@type  graph: graph
	@param graph: Graph.

	@rtype:  list
	@return: Mutual-accessibility matrix
	"""
	accessibility = graph.accessibility()
	grsize = len(accessibility)
	for i in xrange(grsize):
		for j in xrange(grsize - i):
			if (accessibility[i][j] != accessibility[j][i]):
				accessibility[i][j] = 0
				accessibility[i][j] = 0
	return accessibility


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

