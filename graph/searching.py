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
Search algorithms for python-graph.
"""


# Module metadata
__authors__ = "Pedro Matiello"
__license__ = "MIT"


# Imports
import graph


# Depth-first search

def depth_first_search(graph):
	"""
	Depth-first search.

	@type  graph: graph
	@param graph: Graph.

	@rtype:  tuple
	@return: A tupple containing tree lists:
		1. Generated spanning tree
		2. Graph's preordering
		3. Graph's postordering
	"""
	visited = []			# List for marking visited and non-visited nodes
	spanning_tree = []		# Spanning tree
	pre = []				# Graph's preordering
	post = []				# Graph's postordering

	# Initialization
	for each in graph.get_nodes():
		visited.append(0)
		spanning_tree.append(-1)
	
	# Algorithm loop
	for each in graph.get_nodes():
		if (not visited[each]):							# Select a non-visited node
			_dfs(graph, visited, spanning_tree, pre, post, each)	# Explore node's connected component

	return spanning_tree, pre, post


def _dfs(graph, visited, spanning_tree, pre, post, node):
	"""
	Depht-first search subfunction.
	
	@type  graph: graph
	@param graph: Graph.

	@type  visited: list
	@param visited: List of nodes (visited nodes are marked non-zero).

	@type  spanning_tree: list
	@param spanning_tree: Spanning tree being built for the graph by DFS.

	@type  pre: list
	@param pre: Graph's preordering	

	@type  post: list
	@param post: Graph's postordering

	@type  node: number
	@param node: Node to be explored by DFS.
	"""
	visited[node] = 1
	pre.append(node)
	# Explore recursively the connected component
	for each in graph.get_node(node):
		if (not visited[each]):
			spanning_tree[each] = node
			_dfs(graph, visited, spanning_tree, pre, post, each)
	post.append(node)


# Breadth-first search

def breadth_first_search(graph):
	"""
	Breadth-first search.

	@type  graph: graph
	@param graph: Graph.

	@rtype:  list
	@return: Generated spanning_tree
	"""
	queue = []			# Visiting queue
	spanning_tree = []	# Spanning tree

	# Initialization
	for each in graph.get_nodes():
		spanning_tree.append(-2)	# -2 in spanning_tree means a non-visited node

	# Algorithm
	for each in graph.get_nodes():
		if (spanning_tree[each] == -2):
			queue.append(each)
			spanning_tree[each] = -1	# -1 means that the node is the root of a tree

			while (queue != []):
				node = queue.pop(0)

				for other in graph.get_node(node):
					if (spanning_tree[other] == -2):
						queue.append(other)
						spanning_tree[other] = node

	return spanning_tree

