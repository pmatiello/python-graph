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
python-graph
Search algorithms.
"""


# Depht First Search (Recursive implementation)

def depth_first_search(graph):
	"""
	Depht first search.

	Perform DFS:
		1. Select first non-visited node;
		2. Call _dfs() for the selected node (will explore entire connected component)
		3. If there are any non-visited node, go to 1. Otherwise, end.

	@type  graph: graph
	@param graph: Graph.

	@rtype:  list
	@return: Generated spanning_tree
	"""
	visited = []
	spanning_tree = []

	for each in xrange(len(graph)):
		visited.append(0)
		spanning_tree.append(-1)
	
	for each in xrange(len(graph)):
		if (not visited[each]):
			_dfs(graph, visited, spanning_tree, each)

	return spanning_tree


def _dfs(graph, visited, spanning_tree, node):
	"""
	Depht first search subfunction.

	Explore recursively the connected component for the given node.
	
	@type  graph: graph
	@param graph: Graph.

	@type  visited: list
	@param visited: List of nodes (visited nodes are marked non-zero).

	@type  spanning_tree: list
	@param spanning_tree: Spanning tree being built for the graph by DFS.

	@type  node: number
	@param node: Node to be explored by DFS.
	"""
	visited[node] = 1
	for each in graph.get_node(node):
		if (not visited[each]):
			spanning_tree[each] = node
			_dfs(graph, visited, spanning_tree, each)
