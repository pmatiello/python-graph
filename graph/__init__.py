# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
#                         Christian Muise <christian.muise@gmail.com>
#                         Nathan Davis <davisn90210@gmail.com>
#                         Zsolt Haraszti <zsolt@drawwell.net>
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

@version: 1.3.1
"""


# Imports
import accessibility
import generators
import minmax
import searching
import sorting
import readwrite
import traversal


# Graph class --------------------------------------------------------------------------------------

class graph (object):
	"""
	Graph class.
	
	Graphs are built of nodes and edges.

	@sort:  __init__, __getitem__, __iter__, __len__, __str__, add_edge, add_edge_attribute,
	add_graph, add_node, add_node_attribute, add_nodes, add_spanning_tree, complete, del_edge,
	del_node, edges, get_edge_attributes, get_edge_label, get_edge_weight, get_node_attributes,
	has_edge, has_node, inverse, neighbors, nodes, order, set_edge_label, set_edge_weight,
	traversal, generate, read, write, accessibility, breadth_first_search, connected_components,
	cut_edges, cut_nodes, depth_first_search, minimal_spanning_tree, shortest_path
	"""


	def __init__(self):
		"""
		Initialize a graph.
		"""
		self.node_neighbors = {}		# Pairing: Node -> Neighbors
		self.edge_properties = {}		# Pairing: Edge -> (Label, Weight)
		self.node_attr = {}				# Pairing: Node -> Attributes
		self.edge_attr = {}				# Pairing: Edge -> Attributes


	def __str__(self):
		"""
		Return a string representing the graph when requested by str() (or print).

		@rtype:  string
		@return: String representing the graph.
		"""
		return "<graph object " + str(self.nodes()) + " " + str(self.edges()) + ">"


	def __len__(self):
		"""
		Return the order of the graph when requested by len().

		@rtype:  number
		@return: Size of the graph.
		"""
		return len(self.node_neighbors)


	def __iter__(self):
		"""
		Return a iterator passing through all nodes in the graph.
		
		@rtype:  iterator
		@return: Iterator passing through all nodes in the graph.
		"""
		for each in self.node_neighbors.iterkeys():
			yield each


	def __getitem__(self, node):
		"""
		Return a iterator passing through all neighbors of the given node.
		
		@rtype:  iterator
		@return: Iterator passing through all neighbors of the given node.
		"""
		for each in self.node_neighbors[node]:
			yield each


	def read(self, string, fmt='xml'):
		"""
		Read a graph from a string. Nodes and edges specified in the input will be added to the
		current graph.
		
		@type  string: string
		@param string: Input string specifying a graph.

		@type  fmt: string
		@param fmt: Input format. Possible formats are:
			1. 'xml' - XML (default)
		"""
		if (fmt == 'xml'):
			readwrite.read_xml(self, string)


	def write(self, fmt='xml'):
		"""
		Write the graph to a string. Depending of the output format, this string can be used by
		read() to rebuild the graph.
		
		@type  fmt: string
		@param fmt: Output format. Possible formats are:
			1. 'xml' - XML (default)
			2. 'dot' - DOT Language (for GraphViz)
			3. 'dotwt' - DOT Language with weight information

		@rtype:  string
		@return: String specifying the graph.
		"""
		if (fmt == 'xml'):
			return readwrite.write_xml(self)
		elif (fmt == 'dot'):
			return readwrite.write_dot_graph(self, False)
		elif (fmt == 'dotwt'):
			return readwrite.write_dot_graph(self, True)


	def generate(self, num_nodes, num_edges, weight_range=(1, 1)):
		"""
		Add nodes and random edges to the graph.
		
		@type  num_nodes: number
		@param num_nodes: Number of nodes.
		
		@type  num_edges: number
		@param num_edges: Number of edges.

		@type  weight_range: tuple
		@param weight_range: tuple of two integers as lower and upper limits on randomly generated
		weights (uniform distribution).
		"""
		generators.generate(self, num_nodes, num_edges, weight_range)


	def nodes(self):
		"""
		Return node list.

		@rtype:  list
		@return: Node list.
		"""
		return self.node_neighbors.keys()


	def neighbors(self, node):
		"""
		Return all nodes that are directly accessible from given node.

		@type  node: node
		@param node: Node identifier

		@rtype:  list
		@return: List of nodes directly accessible from given node.
		"""
		return self.node_neighbors[node]
	
	
	def edges(self):
		"""
		Return all edges in the graph.
		
		@rtype:  list
		@return: List of all edges in the graph.
		"""
		return self.edge_properties.keys()


	def has_node(self, node):
		"""
		Return whether the requested node exists.

		@type  node: node
		@param node: Node identifier

		@rtype:  boolean
		@return: Truth-value for node existence.
		"""
		return self.node_neighbors.has_key(node)


	def add_node(self, node, attrs=[]):
		"""
		Add given node to the graph.
		
		@attention: While nodes can be of any type, it's strongly recommended to use only numbers
		and single-line strings as node identifiers if you intend to use write().

		@type  node: node
		@param node: Node identifier.
		
		@type  attrs: list
		@param attrs: List of node attributes specified as (attribute, value) tuples.
		"""
		if (not node in self.node_neighbors):
			self.node_neighbors[node] = []
			self.node_attr[node] = attrs


	def add_nodes(self, nodelist):
		"""
		Add given nodes to the graph.
		
		@attention: While nodes can be of any type, it's strongly recommended to use only numbers
		and single-line strings as node identifiers if you intend to use write().

		@type  nodelist: list
		@param nodelist: List of nodes to be added to the graph.
		"""
		for each in nodelist:
			self.add_node(each)


	def add_edge(self, u, v, wt=1, label='', attrs=[]):
		"""
		Add an edge (u,v) to the graph connecting nodes u and v.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		
		@type  wt: number
		@param wt: Edge weight.
		
		@type  label: string
		@param label: Edge label.
		
		@type  attrs: list
		@param attrs: List of node attributes specified as (attribute, value) tuples.
		"""
		if (v not in self.node_neighbors[u] and u not in self.node_neighbors[v]):
			self.node_neighbors[u].append(v)
			self.node_neighbors[v].append(u)
			self.edge_properties[(u, v)] = [label, wt]
			self.edge_properties[(v, u)] = [label, wt]
			self.edge_attr[(u, v)] = attrs
			self.edge_attr[(v, u)] = attrs


	def del_node(self, node):
		"""
		Remove a node from the graph.
		
		@type  node: node
		@param node: Node identifier.
		"""
		for each in list(self.neighbors(node)):
			self.del_edge(each, node)
		del(self.node_neighbors[node])
		del(self.node_attr[node])


	def del_edge(self, u, v):
		"""
		Remove an edge (u, v) from the graph.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		"""
		self.node_neighbors[u].remove(v)
		self.node_neighbors[v].remove(u)
		del(self.edge_properties[(u,v)])
		del(self.edge_properties[(v,u)])
		del(self.edge_attr[(u,v)])
		del(self.edge_attr[(v,u)])


	def get_edge_weight(self, u, v):
		"""
		Get the weight of an edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		
		@rtype:  number
		@return: Edge weight.
		"""
		return self.edge_properties[(u, v)][1]


	def set_edge_weight(self, u, v, wt):
		"""
		Set the weight of an edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@type  wt: number
		@param wt: Edge weight.
		"""
		self.edge_properties[(u, v)][1] = wt
		self.edge_properties[(v, u)][1] = wt


	def get_edge_label(self, u, v):
		"""
		Get the label of an edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		
		@rtype:  string
		@return: Edge label
		"""
		return self.edge_properties[(u, v)][0]


	def set_edge_label(self, u, v, label):
		"""
		Set the label of an edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@type  label: string
		@param label: Edge label.
		"""
		self.edge_properties[(u, v)][0] = label
		self.edge_properties[(v, u)][0] = label
	
	
	def add_node_attribute(self, node, attr):
		"""
		Add attribute to the given node.

		@type  node: node
		@param node: Node identifier

		@type  attr: tuple
		@param attr: Node attribute specified as a tuple in the form (attribute, value).
		"""
		self.node_attr[node] = self.node_attr[node] + [attr]


	def get_node_attributes(self, node):
		"""
		Return the attributes of the given node.

		@type  node: node
		@param node: Node identifier

		@rtype:  list
		@return: List of attributes specified tuples in the form (attribute, value).
		"""
		return self.node_attr[node]


	def add_edge_attribute(self, u, v, attr):
		"""
		Add attribute to the given edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@type  attr: tuple
		@param attr: Node attribute specified as a tuple in the form (attribute, value).
		"""
		self.edge_attr[(u,v)] = self.edge_attr[(u,v)] + [attr]
		self.edge_attr[(v,u)] = self.edge_attr[(v,u)] + [attr]


	def get_edge_attributes(self, u, v):
		"""
		Return the attributes of the given edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@rtype:  list
		@return: List of attributes specified tuples in the form (attribute, value).
		"""
		return self.edge_attr[(u,v)]


	def has_edge(self, u, v):
		"""
		Return whether an edge between nodes u and v exists.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@rtype:  boolean
		@return: Truth-value for edge existence.
		"""
		return self.edge_properties.has_key((u,v)) and self.edge_properties.has_key((v,u))
	
	
	def order(self, node):
		"""
		Return the order of the given node.
		
		@rtype:  number
		@return: Order of the given node.
		"""
		return len(self.neighbors(node))


	def complete(self):
		"""
		Make the graph a complete graph.
		
		@attention: This will modify the current graph.
		"""
		for each in self.nodes():
			for other in self.nodes():
				if (each != other):
					self.add_edge(each, other)


	def inverse(self):
		"""
		Return the inverse of the graph.
		
		@rtype:  graph
		@return: Complement graph for the graph.
		"""
		inv = graph()
		inv.add_nodes(self.nodes())
		inv.complete()
		for each in self.edges():
			if (inv.has_edge(each[0], each[1])):
				inv.del_edge(each[0], each[1])
		return inv


	def add_graph(self, graph):
		"""
		Add other graph to the graph.
		
		@attention: Attributes and labels are not preserved.
		
		@type  graph: graph
		@param graph: Graph
		"""
		self.add_nodes(graph.nodes())
		for each_node in graph.nodes():
			for each_edge in graph.neighbors(each_node):
				self.add_edge(each_node, each_edge)


	def add_spanning_tree(self, st):
		"""
		Add a spanning tree to the graph.
		
		@type  st: dictionary
		@param st: Spanning tree.
		"""
		self.add_nodes(st.keys())
		for each in st:
			if (st[each] is not None):
				self.add_edge(st[each], each)


	def traversal(self, node, order='pre'):
		"""
		Graph traversal iterator.

		@type  node: node
		@param node: Node.
		
		@type  order: string
		@param order: traversal ordering. Possible values are:
			2. 'pre' - Preordering (default)
			1. 'post' - Postordering
		
		@rtype:  iterator
		@return: Traversal iterator.
		"""
		for each in traversal.traversal(self, node, order):
			yield each


	def depth_first_search(self, root=None):
		"""
		Depht-first search.
		
		@type  root: node
		@param root: Optional root node (will explore only root's connected component)

		@rtype:  tuple
		@return:  tupple containing a dictionary and two lists:
			1. Generated spanning tree
			2. Graph's preordering
			3. Graph's postordering
		"""
		return searching.depth_first_search(self, root)


	def breadth_first_search(self, root=None):
		"""
		Breadth-first search.

		@type  root: node
		@param root: Optional root node (will explore only root's connected component)

		@rtype:  dictionary
		@return: A tuple containing a dictionary and a list.
			1. Generated spanning tree
			2. Graph's level-based ordering
		"""
		return searching.breadth_first_search(self, root)


	def accessibility(self):
		"""
		Accessibility matrix (transitive closure).

		@rtype:  dictionary
		@return: Accessibility information for each node.
		"""
		return accessibility.accessibility(self)


	def connected_components(self):
		"""
		Connected components.

		@attention: Indentification of connected components is meaningful only for non-directed
		graphs.

		@rtype:  dictionary
		@return: Pairing that associates each node to its connected component.
		"""
		return accessibility.connected_components(self)


	def minimal_spanning_tree(self, root=None):
		"""
		Minimal spanning tree.

		@type  root: node
		@param root: Optional root node (will explore only root's connected component)

		@attention: Minimal spanning tree meaningful only for weighted graphs.

		@rtype:  list
		@return: Generated spanning tree.
		"""
		return minmax.minimal_spanning_tree(self, root)


	def shortest_path(self, source):
		"""
		Return the shortest path distance between source node and all other nodes using Dijkstra's
		algorithm.
		
		@attention: All weights must be nonnegative.

		@type  source: node
		@param source: Node from which to start the search.

		@rtype:  tuple
		@return: A tuple containing two dictionaries, each keyed by target nodes.
			1. Shortest path spanning tree
			2. Shortest distance from given source to each target node
		Inaccessible target nodes do not appear in either dictionary.
		"""
		return minmax.shortest_path(self, source)
	
	
	def cut_edges(self):
		"""
		Return the cut-edges of the given graph.
		
		@rtype:  list
		@return: List of cut-edges.
		"""
		return accessibility.cut_edges(self)


	def cut_nodes(self):
		"""
		Return the cut-nodes of the given graph.
		
		@rtype:  list
		@return: List of cut-nodes.
		"""
		return accessibility.cut_nodes(self)


# Digraph class ------------------------------------------------------------------------------------

class digraph (object):
	"""
	Digraph class.
	
	Digraphs are built of nodes and directed edges.

	@sort: __init__, __getitem__, __iter__, __len__, __str__, add_edge, add_edge_attribute,
	add_graph, add_node, add_node_attribute, add_nodes, add_spanning_tree, complete, degree,
	del_edge, del_node, edges, get_edge_attributes, get_edge_label, get_edge_weight,
	get_node_attributes, has_edge, has_node, incidents, inverse, neighbors, nodes, order,
	set_edge_label, set_edge_weight, traversal, generate, read, write, accessibility,
	breadth_first_search, cut_edges, cut_nodes, depth_first_search, minimal_spanning_tree,
	mutual_accessibility, shortest_path, topological_sorting
	"""


	def __init__(self):
		"""
		Initialize a digraph.
		"""
		self.node_neighbors = {}	# Pairing: Node -> Neighbors
		self.edge_properties = {}	# Pairing: Edge -> (Label, Weight)
		self.node_incidence = {}	# Pairing: Node -> Incident nodes
		self.node_attr = {}			# Pairing: Node -> Attributes
		self.edge_attr = {}			# Pairing: Edge -> Attributes


	def __str__(self):
		"""
		Return a string representing the digraph when requested by str() (or print).

		@rtype:  string
		@return: String representing the graph.
		"""
		return "<graph object " + str(self.nodes()) + " " + str(self.edges()) + ">"


	def __len__(self):
		"""
		Return the order of the digraph when requested by len().

		@rtype:  number
		@return: Size of the graph.
		"""
		return len(self.node_neighbors)


	def __iter__(self):
		"""
		Return a iterator passing through all nodes in the digraph.
		
		@rtype:  iterator
		@return: Iterator passing through all nodes in the digraph.
		"""
		for each in self.node_neighbors.iterkeys():
			yield each


	def __getitem__(self, node):
		"""
		Return a iterator passing through all neighbors of the given node.
		
		@rtype:  iterator
		@return: Iterator passing through all neighbors of the given node.
		"""
		for each in self.node_neighbors[node]:
			yield each


	def read(self, string, fmt='xml'):
		"""
		Read a graph from a string. Nodes and edges specified in the input will be added to the
		current graph.
		
		@type  string: string
		@param string: Input string specifying a graph.

		@type  fmt: string
		@param fmt: Input format. Possible formats are:
			1. 'xml' - XML (default)
		"""
		if (fmt == 'xml'):
			readwrite.read_xml(self, string)


	def write(self, fmt='xml'):
		"""
		Write the graph to a string. Depending of the output format, this string can be used by
		read() to rebuild the graph.
		
		@type  fmt: string
		@param fmt: Output format. Possible formats are:
			1. 'xml' - XML (default)
			2. 'dot' - DOT Language (for GraphViz)
			3. 'dotwt' - DOT Language with weight information

		@rtype:  string
		@return: String specifying the graph.
		"""
		if (fmt == 'xml'):
			return readwrite.write_xml(self)
		elif (fmt == 'dot'):
			return readwrite.write_dot_digraph(self, False)
		elif (fmt == 'dotwt'):
			return readwrite.write_dot_digraph(self, True)


	def generate(self, num_nodes, num_edges, weight_range=(1, 1)):
		"""
		Add nodes and random edges to the graph.
		
		@type  num_nodes: number
		@param num_nodes: Number of nodes.
		
		@type  num_edges: number
		@param num_edges: Number of edges.

		@type  weight_range: tuple
		@param weight_range: tuple of two integers as lower and upper limits on randomly generated
		weights (uniform distribution).
		"""
		generators.generate(self, num_nodes, num_edges, weight_range)


	def nodes(self):
		"""
		Return node list.

		@rtype:  list
		@return: Node list.
		"""
		return self.node_neighbors.keys()


	def neighbors(self, node):
		"""
		Return all nodes that are directly accessible from given node.

		@type  node: node
		@param node: Node identifier

		@rtype:  list
		@return: List of nodes directly accessible from given node.
		"""
		return self.node_neighbors[node]
	
	
	def incidents(self, node):
		"""
		Return all nodes that are incident to the given node.
		
		@type  node: node
		@param node: Node identifier

		@rtype:  list
		@return: List of nodes directly accessible from given node.	
		"""
		return self.node_incidence[node]
		
	
	
	def edges(self):
		"""
		Return all edges in the graph.
		
		@rtype:  list
		@return: List of all edges in the graph.
		"""
		return self.edge_properties.keys()


	def has_node(self, node):
		"""
		Return whether the requested node exists.

		@type  node: node
		@param node: Node identifier

		@rtype:  boolean
		@return: Truth-value for node existence.
		"""
		return self.node_neighbors.has_key(node)


	def add_node(self, node, attrs=[]):
		"""
		Add given node to the graph.
		
		@attention: While nodes can be of any type, it's strongly recommended to use only numbers
		and single-line strings as node identifiers if you intend to use write().

		@type  node: node
		@param node: Node identifier.
		
		@type  attrs: list
		@param attrs: List of node attributes specified as (attribute, value) tuples.
		"""
		if (node not in self.node_neighbors):
			self.node_neighbors[node] = []
			self.node_incidence[node] = []
			self.node_attr[node] = attrs


	def add_nodes(self, nodelist):
		"""
		Add given nodes to the graph.
		
		@attention: While nodes can be of any type, it's strongly recommended to use only numbers
		and single-line strings as node identifiers if you intend to use write().

		@type  nodelist: list
		@param nodelist: List of nodes to be added to the graph.
		"""
		for each in nodelist:
			self.add_node(each)


	def add_edge(self, u, v, wt=1, label='', attrs=[]):
		"""
		Add an directed edge (u,v) to the graph connecting nodes u to v.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		
		@type  wt: number
		@param wt: Edge weight.
		
		@type  label: string
		@param label: Edge label.
		
		@type  attrs: list
		@param attrs: List of node attributes specified as (attribute, value) tuples.
		"""
		if (v not in self.node_neighbors[u]):
			self.node_neighbors[u].append(v)
			self.node_incidence[v].append(u)
			self.edge_properties[(u, v)] = [label, wt]
			self.edge_attr[(u, v)] = attrs


	def del_node(self, node):
		"""
		Remove a node from the graph.
		
		@type  node: node
		@param node: Node identifier.
		"""
		for each in list(self.incidents(node)):
			self.del_edge(each, node)
		for each in list(self.neighbors(node)):
			self.del_edge(node, each)
		del(self.node_neighbors[node])
		del(self.node_incidence[node])
		del(self.node_attr[node])


	def del_edge(self, u, v):
		"""
		Remove an directed edge (u, v) from the graph.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		"""
		self.node_neighbors[u].remove(v)
		self.node_incidence[v].remove(u)
		del(self.edge_properties[(u,v)])
		del(self.edge_attr[(u,v)])


	def get_edge_weight(self, u, v):
		"""
		Get the weight of an edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		
		@rtype:  number
		@return: Edge weight.
		"""
		return self.edge_properties[(u, v)][1]


	def set_edge_weight(self, u, v, wt):
		"""
		Set the weight of an edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@type  wt: number
		@param wt: Edge weight.
		"""
		self.edge_properties[(u, v)][1] = wt


	def get_edge_label(self, u, v):
		"""
		Get the label of an edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		
		@rtype:  string
		@return: Edge label
		"""
		return self.edge_properties[(u, v)][0]


	def set_edge_label(self, u, v, label):
		"""
		Set the label of an edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@type  label: string
		@param label: Edge label.
		"""
		self.edge_properties[(u, v)][0] = label
	
	
	def add_node_attribute(self, node, attr):
		"""
		Add attribute to the given node.

		@type  node: node
		@param node: Node identifier

		@type  attr: tuple
		@param attr: Node attribute specified as a tuple in the form (attribute, value).
		"""
		self.node_attr[node] = self.node_attr[node] + [attr]


	def get_node_attributes(self, node):
		"""
		Return the attributes of the given node.

		@type  node: node
		@param node: Node identifier

		@rtype:  list
		@return: List of attributes specified tuples in the form (attribute, value).
		"""
		return self.node_attr[node]


	def add_edge_attribute(self, u, v, attr):
		"""
		Add attribute to the given edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@type  attr: tuple
		@param attr: Node attribute specified as a tuple in the form (attribute, value).
		"""
		self.edge_attr[(u,v)] = self.edge_attr[(u,v)] + [attr]


	def get_edge_attributes(self, u, v):
		"""
		Return the attributes of the given edge.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@rtype:  list
		@return: List of attributes specified tuples in the form (attribute, value).
		"""
		return self.edge_attr[(u,v)]


	def has_edge(self, u, v):
		"""
		Return whether an edge between nodes u and v exists.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@rtype:  boolean
		@return: Truth-value for edge existence.
		"""
		return self.edge_properties.has_key((u,v))

	
	def order(self, node):
		"""
		Return the order of the given node.
		
		@rtype:  number
		@return: Order of the given node.
		"""
		return len(self.neighbors(node))


	def degree(self, node):
		"""
		Return the degree of the given node.
		
		@rtype:  number
		@return: Order of the given node.
		"""
		return len(self.node_incidence[node])


	def complete(self):
		"""
		Make the graph a complete graph.
		
		@attention: This will modify the current graph.
		"""
		for each in self.nodes():
			for other in self.nodes():
				if (each != other):
					self.add_edge(each, other)


	def inverse(self):
		"""
		Return the inverse of the graph.
		
		@rtype:  graph
		@return: Complement graph for the graph.
		"""
		inv = digraph()
		inv.add_nodes(self.nodes())
		inv.complete()
		for each in self.edges():
			inv.del_edge(each[0], each[1])
		return inv


	def add_graph(self, graph):
		"""
		Add other graph to the graph.
		
		@attention: Attributes and labels are not preserved.
		
		@type  graph: graph
		@param graph: Graph
		"""
		self.add_nodes(graph.nodes())
		for each_node in graph.nodes():
			for each_edge in graph.neighbors(each_node):
				self.add_edge(each_node, each_edge)


	def add_spanning_tree(self, st):
		"""
		Add a spanning tree to the graph.
		
		@type  st: dictionary
		@param st: Spanning tree.
		"""
		self.add_nodes(st.keys())
		for each in st:
			if (st[each] is not None):
				self.add_edge(st[each], each)


	def traversal(self, node, order='pre'):
		"""
		Graph traversal iterator.

		@type  node: node
		@param node: Node.
		
		@type  order: string
		@param order: traversal ordering. Possible values are:
			2. 'pre' - Preordering (default)
			1. 'post' - Postordering
		
		@rtype:  iterator
		@return: Traversal iterator.
		"""
		for each in traversal.traversal(self, node, order):
			yield each


	def depth_first_search(self, root=None):
		"""
		Depht-first search.
		
		@type  root: node
		@param root: Optional root node (will explore only root's connected component)

		@rtype:  tuple
		@return:  tupple containing a dictionary and two lists:
			1. Generated spanning tree
			2. Graph's preordering
			3. Graph's postordering
		"""
		return searching.depth_first_search(self, root)


	def accessibility(self):
		"""
		Accessibility matrix (transitive closure).

		@rtype:  dictionary
		@return: Accessibility information for each node.
		"""
		return accessibility.accessibility(self)


	def breadth_first_search(self, root=None):
		"""
		Breadth-first search.

		@type  root: node
		@param root: Optional root node (will explore only root's connected component)

		@rtype:  dictionary
		@return: A tuple containing a dictionary and a list.
			1. Generated spanning tree
			2. Graph's level-based ordering
		"""
		return searching.breadth_first_search(self, root)


	def mutual_accessibility(self):
		"""
		Mutual-accessibility matrix (strongly connected components).

		@rtype:  list
		@return: Mutual-accessibility information for each node.
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


	def minimal_spanning_tree(self, root=None):
		"""
		Minimal spanning tree.

		@type  root: node
		@param root: Optional root node (will explore only root's connected component)

		@attention: Minimal spanning tree meaningful only for weighted graphs.

		@rtype:  list
		@return: Generated spanning tree.
		"""
		return minmax.minimal_spanning_tree(self, root)


	def shortest_path(self, source):
		"""
		Return the shortest path distance between source node and all other nodes using Dijkstra's
		algorithm.
		
		@attention: All weights must be nonnegative.

		@type  source: node
		@param source: Node from which to start the search.

		@rtype:  tuple
		@return: A tuple containing two dictionaries, each keyed by target nodes.
			1. Shortest path spanning tree
			2. Shortest distance from given source to each target node
		Inaccessible target nodes do not appear in either dictionary.
		"""
		return minmax.shortest_path(self, source)
	
	
	def cut_edges(self):
		"""
		Return the cut-edges of the given graph.
		
		@rtype:  list
		@return: List of cut-edges.
		"""
		return accessibility.cut_edges(self)


	def cut_nodes(self):
		"""
		Return the cut-nodes of the given graph.
		
		@rtype:  list
		@return: List of cut-nodes.
		"""
		return accessibility.cut_nodes(self)


# Hypergraph class ---------------------------------------------------------------------------------

class hypergraph (object):
	"""
	Hypergraph class.
	
	Hypergraphs are a generalization of graphs where an edge (called hyperedge) can connect more
	than two nodes.
	
	@sort: __init__, __len__, __str__, add_hyperedge, add_hyperedges, add_node,	add_nodes, has_node,
	hyperedges, link, links, nodes, unlink, read, write, accessibility,	connected_components,
	cut_hyperedges, cut_nodes
	"""


	def __init__(self):
		"""
		Initialize a hypergraph.
		"""
		self.node_links = {}	# Pairing: Node -> Hyperedge
		self.edge_links = {} 	# Pairing: Hyperedge -> Node
		self.graph = graph()	# Ordinary graph


	def __str__(self):
		"""
		Return a string representing the hypergraph when requested by str() (or print).

		@rtype:  string
		@return: String representing the hypergraph.
		"""
		return "<hypergraph object " + str(self.nodes()) + " " + str(self.edge_links) + ">"


	def __len__(self):
		"""
		Return the size of the hypergraph when requested by len().

		@rtype:  number
		@return: Size of the hypergraph.
		"""
		return len(self.node_links)


	def read(self, string, fmt='xml'):
		"""
		Read a hypergraph from a string. Nodes and hyperedges specified in the input will be added
		to the current graph.
		
		@type  string: string
		@param string: Input string specifying a graph.

		@type  fmt: string
		@param fmt: Input format. Possible formats are:
			1. 'xml' - XML (default)
		"""
		if (fmt == 'xml'):
			readwrite.read_xml_hypergraph(self, string)


	def write(self, fmt='xml'):
		"""
		Write the hypergraph to a string. Depending of the output format, this string can be used by
		read() to rebuild the graph.
		
		@type  fmt: string
		@param fmt: Output format. Possible formats are:
			1. 'xml' - XML (default)
			2. 'dot' - DOT Language (for GraphViz)
			3. 'dotclr' - DOT Language, coloured

		@rtype:  string
		@return: String specifying the graph.
		"""
		if (fmt == 'xml'):
			return readwrite.write_xml_hypergraph(self)
		elif (fmt == 'dot'):
			return readwrite.write_dot_hypergraph(self)
		elif (fmt == 'dotclr'):
			return readwrite.write_dot_hypergraph(self, coloured=True)
	

	def nodes(self):
		"""
		Return node list.
		
		@rtype:  list
		@return: Node list.
		"""
		return self.node_links.keys()


	def hyperedges(self):
		"""
		Return hyperedge list.

		@rtype:  list
		@return: List of hyperedges linked to the given node.
		"""
		return self.edge_links.keys()


	def links(self, obj):
		"""
		Return all objects linked to the given one.
		
		If given a node, linked hyperedges will be returned. If given a hyperedge, linked nodes will
		be returned.
		
		@type  obj: node or hyperedge
		@param obj: Object identifier.
		
		@rtype:  list
		@return: List of objects linked to the given one.
		"""
		if (obj in self.node_links):
			return self.node_links[obj]
		else:
			return self.edge_links[obj]


	def has_node(self, node):
		"""
		Return whether the requested node exists.

		@type  node: node
		@param node: Node identifier

		@rtype:  boolean
		@return: Truth-value for node existence.
		"""
		return self.node_links.has_key(node)


	def add_node(self, node):
		"""
		Add given node to the hypergraph.
		
		@attention: While nodes can be of any type, it's strongly recommended to use only numbers
		and single-line strings as node identifiers if you intend to use write().

		@type  node: node
		@param node: Node identifier.
		"""
		if (not node in self.node_links):
			self.node_links[node] = []
			self.graph.add_node((node,'n'))


	def add_nodes(self, nodelist):
		"""
		Add given nodes to the hypergraph.
		
		@attention: While nodes can be of any type, it's strongly recommended to use only numbers
		and single-line strings as node identifiers if you intend to use write().

		@type  nodelist: list
		@param nodelist: List of nodes to be added to the graph.
		"""
		for each in nodelist:
			self.add_node(each)


	def add_hyperedge(self, hyperedge):
		"""
		Add given hyperedge to the hypergraph.

		@attention: While hyperedge-nodes can be of any type, it's strongly recommended to use only
		numbers and single-line strings as node identifiers if you intend to use write().
		
		@type  hyperedge: hyperedge
		@param hyperedge: Hyperedge identifier.
		"""
		if (not hyperedge in self.edge_links):
			self.edge_links[hyperedge] = []
			self.graph.add_node((hyperedge,'h'))


	def add_hyperedges(self, edgelist):
		"""
		Add given hyperedges to the hypergraph.

		@attention: While hyperedge-nodes can be of any type, it's strongly recommended to use only
		numbers and single-line strings as node identifiers if you intend to use write().
		
		@type  edgelist: list
		@param edgelist: List of hyperedge-nodes to be added to the graph.
		"""
		for each in edgelist:
			self.add_hyperedge(each)


	def link(self, node, hyperedge):
		"""
		Link given node and hyperedge.

		@type  node: node
		@param node: Node.

		@type  hyperedge: node
		@param hyperedge: Hyperedge.
		"""
		if (hyperedge not in self.node_links[node]):
			self.node_links[node].append(hyperedge)
			self.edge_links[hyperedge].append(node)
			self.graph.add_edge((node,'n'), (hyperedge,'h'))


	def unlink(self, node, hyperedge):
		"""
		Unlink given node and hyperedge.

		@type  node: node
		@param node: Node.

		@type  hyperedge: hyperedge
		@param hyperedge: Hyperedge.
		"""
		self.node_links[node].remove(hyperedge)
		self.edge_links[hyperedge].remove(node)


	def accessibility(self):
		"""
		Accessibility matrix (transitive closure).

		@rtype:  dictionary
		@return: Accessibility information for each node.
		"""
		access_ = accessibility.accessibility(self.graph)
		access = {}
		
		for each in access_.keys():
			if (each[1] == 'n'):
				access[each[0]] = []
				for other in access_[each]:
					if (other[1] == 'n'):
						access[each[0]].append(other[0])
		
		return access

	
	def connected_components(self):
		"""
		Connected components.

		@rtype:  dictionary
		@return: Pairing that associates each node to its connected component.
		"""
		components_ = accessibility.connected_components(self.graph)
		components = {}
		
		for each in components_.keys():
			if (each[1] == 'n'):
				components[each[0]] = components_[each]
		
		return components

	
	def cut_nodes(self):
		"""
		Return the cut-nodes of the given hypergraph.
		
		@rtype:  list
		@return: List of cut-nodes.
		"""
		cut_nodes_ = accessibility.cut_nodes(self.graph)
		cut_nodes = []
		
		for each in cut_nodes_:
			if (each[1] == 'n'):
				cut_nodes.append(each[0])
		
		return cut_nodes


	def cut_hyperedges(self):
		"""
		Return the cut-hyperedges of the given hypergraph.
		
		@rtype:  list
		@return: List of cut-nodes.
		"""
		cut_nodes_ = accessibility.cut_nodes(self.graph)
		cut_nodes = []
		
		for each in cut_nodes_:
			if (each[1] == 'h'):
				cut_nodes.append(each[0])
		
		return cut_nodes
		
	def rank(self):
		"""
		Return the rank of the given hypergraph.
		
		@rtype:  int
		@return: Rank of graph.
		"""
		max_rank = 0
		
		for each in hyperedges:
			if len(each) > max_rank:
				max_rank = len(each)
				
		return max_rank
