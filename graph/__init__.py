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

A library for working with graphs in Python.
"""


# Module metadata
__authors__ = "Pedro Matiello"
__license__ = "MIT"


# Imports
import searching
import accessibility
import sorting


class graph:
	"""
	Graph class.

	Basic operations are defined in this file.
	Algorithms should refer to external files.
	"""


	def __init__(self):
		"""
		Initialize a graph.
		"""
		self.nodes = []		# Arrow/Edge lists	(like an adjacency list)
		self.weights = {}	# Arrow/Edge weight list


	def __str__(self):
		"""
		Return a string representing the graph when requested by str() (or print).

		@rtype:  string
		@return: String representing the graph.
		"""
		return str(self.nodes)


	def __len__(self):
		"""
		Return the size of the graph when requested by len().

		@rtype:  number
		@return: Size of the graph.
		"""
		return len(self.nodes)


	def get_nodes(self):
		"""
		Return node list.

		@rtype:  list
		@return: Node list.
		"""
		return xrange(len(self.nodes))


	def get_node(self, node):
		"""
		Return requested node.

		@type  node: number
		@param node: Node number

		@rtype:  list
		@return: List of nodes directly accessible from given node.
		"""
		return self.nodes[node]


	def add_nodes(self, num):
		"""
		Create num nodes.

		@type  num: number
		@param num: Number of nodes to be added to the graph.
		"""
		while (num > 0):
			self.nodes.append([])
			num = num - 1


	def add_edge(self, u, v):
		"""
		Add an edge (u,v) to the graph connecting nodes u and v.

		@attention: this function should not be used in directed graphs: use add_arrow() instead.

		@type  u: number
		@param u: One node.

		@type  v: number
		@param v: Other node.
		"""
		if (v not in self.nodes[u]):
			self.nodes[u].append(v)
			self.nodes[v].append(u)
			self.weights[(u, v)] = 1
			self.weights[(v, u)] = 1


	def add_arrow(self, u, v):
		"""
		Add an arrow (u,v) to the directed graph connecting node u to node v.

		@type  u: number
		@param u: One node.

		@type  v: number
		@param v: Other node.
		"""
		if (v not in self.nodes[u]):
			self.nodes[u].append(v)
			self.weights[(u, v)] = 1


	def del_edge(self, u, v):
		"""
		Remove an edge (u, v) from the graph.

		@attention: this function should not be used in directed graphs: use del_arrow() instead.

		@type  u: number
		@param u: One node.

		@type  v: number
		@param v: Other node.
		"""
		if (v in self.nodes[u]):
			self.nodes[u].remove(v)
			self.nodes[v].remove(u)
			del(self.weights[(u,v)])
			del(self.weights[(v,u)])


	def del_arrow(self, u, v):
		"""
		Remove an arrow (u, v) from the directed graph.

		@type  u: number
		@param u: One node.

		@type  v: number
		@param v: Other node.
		"""
		if (v in self.nodes[u]):
			self.nodes[u].remove(v)
			del(self.weights[(u,v)])


	def set_edge_weight(self, u, v, w):
		"""
		Set the weight of an edge.

		@type  u: number
		@param u: One node.

		@type  v: number
		@param v: Other node.
		"""
		self.weights[(u, v)] = w
		self.weights[(v, u)] = w


	def set_arrow_weight(self, u, v, w):
		"""
		Set the weight of an arrow.

		@type  u: number
		@param u: One node.

		@type  v: number
		@param v: Other node.
		"""
		self.weights[(u, v)] = w


	def depth_first_search(self):
		"""
		Depht-first search.

		@rtype:  tuple
		@return: A tupple containing tree lists:
			1. Generated spanning tree
			2. Graph's preordering
			3. Graph's postordering
		"""
		return searching.depth_first_search(self)


	def breadth_first_search(self):
		"""
		Breadth-first search.

		@rtype:  list
		@return: Generated spanning_tree
		"""
		return searching.breadth_first_search(self)


	def accessibility(self):
		"""
		Accessibility matrix (transitive closure).

		@rtype:  list
		@return: Accessibility matrix
		"""
		return accessibility.accessibility(self)


	def mutual_accessibility(self):
		"""
		Mutual-accessibility matrix (strongly connected components).

		@rtype:  list
		@return: Mutual-accessibility matrix
		"""
		return accessibility.mutual_accessibility(self)


	def topological_sorting(self):
		"""
		Topological sorting.

		@attention: Topological sorting is meaningful only for directed acyclic graphs.

		@rtype:  list
		@return: Topological sorting for the graph.
		"""
		return sorting.topological_sorting(self)


	def connected_components(self):
		"""
		Connected components.

		@attention: Indentification of connected components is meaningful only for non-directed graphs.

		@rtype:  list
		@return: List that associates each node to its connected component.
		"""
		return accessibility.connected_components(self)
