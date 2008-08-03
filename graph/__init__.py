# Copyright (c) 2007-2008 Pedro Matiello <pmatiello@gmail.com>
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
import accessibility
import generators
import minmax
import searching
import sorting
import readwrite


# Graph class

class graph:
	"""
	Graph class.
	
	Graphs are built of nodes and edges (or arrows).

	@sort: __init__, __len__, __str__, generate, read, write, add_arrow, add_edge, add_graph, add_node, add_nodes, add_spanning_tree, del_arrow, del_edge, get_arrow_weight, get_edge_weight, get_edges, get_nodes, has_arrow, has_edge, has_node, accessibility, breadth_first_search, connected_components, cut_edges, cut_nodes, depth_first_search, minimal_spanning_tree, mutual_accessibility, shortest_path, topological_sorting
	"""


	def __init__(self):
		"""
		Initialize a graph.
		"""
		self.nodes = {}		# Arrow/Edge lists	(like an adjacency list)
		self.weights = {}	# Arrow/Edge weight list


	def __str__(self):
		"""
		Return a string representing the graph when requested by str() (or print).

		@rtype:  string
		@return: String representing the graph.
		"""
		return "<graph object " + str(self.get_nodes()) + " " + str(self.weights) + ">"


	def __len__(self):
		"""
		Return the size of the graph when requested by len().

		@rtype:  number
		@return: Size of the graph.
		"""
		return len(self.nodes)
	

	def read(self, string, fmt=None):
		"""
		Read a graph from a string. Nodes and arrows specified in the input will be added to the current graph.
		
		@type  string: string
		@param string: Input string specifying a graph.

		@type  fmt: string
		@param fmt: Input format. Possible formats are:
			1. 'xml' - XML (default)
		"""
		readwrite.read(self, string, fmt)	


	def write(self, fmt=None):
		"""
		Write the graph to a string. Depending of the output format, this string can be used by read() to rebuild the graph.
		
		@type  fmt: string
		@param fmt: Output format. Possible formats are:
			1. 'xml' - XML (default)
			2. 'dot' - DOT Language (for GraphViz)
			3. 'dotwt' - DOT Language with weight information

		@rtype:  string
		@return: String specifying the graph.
		"""
		return readwrite.write(self, fmt)
	
	
	def generate(self, num_nodes, num_edges, directed=False):
		"""
		Add nodes and random edges to the graph.
		
		@type  num_nodes: number
		@param num_nodes: Number of nodes.
		
		@type  num_edges: number
		@param num_edges: Number of edges.
	
		@type  directed: boolean
		@param directed: Wether the generated graph should be directed or not.
		"""
		generators.generate(self, num_nodes, num_edges, directed)


	def get_nodes(self):
		"""
		Return node list.

		@rtype:  list
		@return: Node list.
		"""
		return self.nodes.keys()


	def get_edges(self, node):
		"""
		Return all outgoing edges from given node.

		@type  node: node
		@param node: Node identifier

		@rtype:  list
		@return: List of nodes directly accessible from given node.
		"""
		return self.nodes[node]


	def has_node(self, node):
		"""
		Return whether the requested node exists.

		@type  node: node
		@param node: Node identifier

		@rtype:  boolean
		@return: Truth-value for node existence.
		"""
		return self.nodes.has_key(node)


	def add_node(self, node):
		"""
		Add given node to the graph.
		
		@attention: While nodes can be of any type, it's strongly recommended to use only numbers and single-line strings as node identifiers if you intend to use write().

		@type  node: node
		@param node: Node identifier.
		"""
		if (not node in self.nodes.keys()):
			self.nodes[node] = []


	def add_nodes(self, nodelist):
		"""
		Add given nodes to the graph.
		
		@attention: While nodes can be of any type, it's strongly recommended to use only numbers and single-line strings as node identifiers if you intend to use write().

		@type  nodelist: list
		@param nodelist: List of nodes to be added to the graph.
		"""
		for each in nodelist:
			if (not each in self.nodes.keys()):
				self.nodes[each] = []


	def add_edge(self, u, v, wt=1):
		"""
		Add an edge (u,v) to the graph connecting nodes u and v.

		@attention: This function should not be used in directed graphs: use add_arrow() instead.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		
		@type  wt: number
		@param wt: Edge weight.
		
		"""
		if (v not in self.nodes[u] and u not in self.nodes[v]):
			self.nodes[u].append(v)
			self.nodes[v].append(u)
			self.weights[(u, v)] = wt
			self.weights[(v, u)] = wt


	def add_arrow(self, u, v, wt=1):
		"""
		Add an arrow (u,v) to the directed graph connecting node u to node v.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@type  wt: number
		@param wt: Arrow weight.
		"""
		if (v not in self.nodes[u]):
			self.nodes[u].append(v)
			self.weights[(u, v)] = wt


	def del_edge(self, u, v):
		"""
		Remove an edge (u, v) from the graph.

		@attention: This function should not be used in directed graphs: use del_arrow() instead.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		"""
		self.nodes[u].remove(v)
		self.nodes[v].remove(u)
		del(self.weights[(u,v)])
		del(self.weights[(v,u)])


	def del_arrow(self, u, v):
		"""
		Remove an arrow (u, v) from the directed graph.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		"""
		self.nodes[u].remove(v)
		del(self.weights[(u,v)])


	def get_arrow_weight(self, u, v):
		"""
		Get the weight of an arrow.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		
		@rtype:  number
		@return: Arrow weight
		"""
		return self.weights[(u, v)]


	def get_edge_weight(self, u, v):
		"""
		Get the weight of an arrow.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.
		
		@rtype:  number
		@return: Edge weight
		"""
		return self.weights[(u, v)]


	def has_arrow(self, u, v):
		"""
		Return whether an arrow from node u to node v exists.

		@type  u: node
		@param u: One node.

		@type  v: node
		@param v: Other node.

		@rtype:  boolean
		@return: Truth-value for arrow existence.
		"""
		return self.weights.has_key((u,v))


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
		return self.weights.has_key((u,v)) and self.weights.has_key((v,u))


	def add_graph(self, graph):
		"""
		Add other graph to the graph.
		
		@type  graph: graph
		@param graph: Graph
		"""
		self.add_nodes(graph.get_nodes())
		for each_node in graph.get_nodes():
			for each_arrow in graph.get_edges(each_node):
				self.add_arrow(each_node, each_arrow)


	def add_spanning_tree(self, st):
		"""
		Add a spanning tree to the graph.
		
		@type  st: dictionary
		@param st: Spanning tree.
		"""
		self.add_nodes(st.keys())
		for each in st:
			if (st[each]):
				self.add_arrow(st[each], each)


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
		@return: Generated spanning tree
		"""
		return searching.breadth_first_search(self, root)


	def accessibility(self):
		"""
		Accessibility matrix (transitive closure).

		@rtype:  dictionary
		@return: Accessibility information for each node.
		"""
		return accessibility.accessibility(self)


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


	def connected_components(self):
		"""
		Connected components.

		@attention: Indentification of connected components is meaningful only for non-directed graphs.

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
		Return the shortest path distance between source node and all other nodes using Dijkstra's algorithm.
		
		@attention: All weights must be nonnegative.

		@type  source: node
		@param source: Node from which to start the search.

		@rtype:  tuple
		@return: A tuple containing two dictionaries, each keyed by target nodes.
			1. Shortest path spanning tree (each key points to previous node in the shortest path transversal)
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


# Hypergraph class

class hypergraph:
	"""
	Hypergraph class.
	
	Hypergraphs are a generalization of graphs where an edge can connect more than two nodes.
	
	To allow that, a structure called hyperedge-node is used here. Ordinary edges then link real nodes to hyperedge-nodes. A hyperedge, as usually understood, is composed of a hyperedge-node and all edges that link to it.
	
	@attention: This class is still experimental and incomplete (most functions are stubs).
	
	@sort: __init__, __len__, __str__, generate, read, write, add_edge, add_hyperedge, add_hyperedges, add_hypergraph, add_node, add_nodes, del_edge, get_edge_weight, get_edges, get_nodes, has_edge, has_node, accessibility, breadth_first_search, connected_components, cut_edges, cut_nodes, depth_first_search, minimal_spanning_tree, mutual_accessibility, shortest_path, topological_sorting
	"""


	def __init__(self):
		"""
		Initialize a hypergraph.
		"""
		self.nodes = {}			# Real nodes
		self.edges = {}			# Ordinary edges (between nodes and hyperedges)
		self.hyperedges = {} 	# Hyperedge-nodes
		self.weights = {}		# Hyperedge weight list


	def __str__(self):
		"""
		Return a string representing the hypergraph when requested by str() (or print).

		@rtype:  string
		@return: String representing the hypergraph.
		"""
		return "<hypergraph object " + str(self.get_nodes()) + " " + str(self.get_hyperedges()) + " " + str(self.weights) + ">"


	def __len__(self):
		"""
		Return the size of the hypergraph when requested by len().

		@rtype:  number
		@return: Size of the hypergraph.
		"""
		return len(self.nodes)


	def read(self, string, fmt=None):
		"""
		TODO
		
		Read a graph from a string. Nodes and arrows specified in the input will be added to the current graph.
		
		@type  string: string
		@param string: Input string specifying a graph.

		@type  fmt: string
		@param fmt: Input format. Possible formats are:
			1. 'xml' - XML (default)
		"""
		pass


	def write(self, fmt=None):
		"""
		TODO

		Write the graph to a string. Depending of the output format, this string can be used by read() to rebuild the graph.
		
		@type  fmt: string
		@param fmt: Output format. Possible formats are:
			1. 'xml' - XML (default)
			2. 'dot' - DOT Language (for GraphViz)
			3. 'dotwt' - DOT Language with weight information

		@rtype:  string
		@return: String specifying the graph.
		"""
		pass
	
	
	def generate(self, num_nodes, num_edges, directed=False):
		"""
		TODO
		
		Add nodes and random edges to the graph.
		
		@type  num_nodes: number
		@param num_nodes: Number of nodes.
		
		@type  num_edges: number
		@param num_edges: Number of edges.
	
		@type  directed: boolean
		@param directed: Wether the generated graph should be directed or not.
		"""
		pass


	def get_nodes(self, real=True, hyperedge=True):
		"""
		Return node list.
		
		@type  real: boolean
		@param real: Wether real nodes should be returned in the list.

		@type  hyperedge: boolean
		@param hyperedge: Wether hyperedge-nodes should be returned in the list.

		@rtype:  list
		@return: Node list.
		"""
		if (real and hyperedge):
			return self.nodes.keys() + self.hyperedges.keys()
		elif (real and not hyperedge):
			return self.nodes.keys()
		elif (not real and hyperedge):
			return self.hyperedges
		else:
			return []


	def get_edges(self, node, follow=False):
		"""
		Return all outgoing edges from given node.
		
		@type  follow: boolean
		@param follow: If set to true, will discover and return adjacent real nodes instead of hyperedge-nodes.

		@type  node: node
		@param node: Node identifier

		@rtype:  list
		@return: List of nodes directly accessible from given node.
		"""
		if (node in self.nodes):
			if (follow):
				reply = []
				for each in self.nodes[node]:
					reply = reply + self.hyperedges[each]
				return reply
			else:
				return self.nodes[node]
		else:
			return self.hyperedges[node]


	def has_node(self, node):
		"""
		Return whether the requested node exists.

		@type  node: node
		@param node: Node identifier

		@rtype:  boolean
		@return: Truth-value for node existence.
		"""
		return (self.nodes.has_key(node) or self.hyperedges.has_key(node))


	def add_node(self, node):
		"""
		Add given real node to the hypergraph.
		
		@attention: While nodes can be of any type, it's strongly recommended to use only numbers and single-line strings as node identifiers if you intend to use write().

		@type  node: node
		@param node: Node identifier.
		"""
		if (not node in self.nodes.keys()):
			self.nodes[node] = []


	def add_nodes(self, nodelist):
		"""
		Add given real nodes to the hypergraph.
		
		@attention: While nodes can be of any type, it's strongly recommended to use only numbers and single-line strings as node identifiers if you intend to use write().

		@type  nodelist: list
		@param nodelist: List of nodes to be added to the graph.
		"""
		for each in nodelist:
			if (not each in self.nodes.keys()):
				self.nodes[each] = []


	def add_hyperedge(self, hyperedge, wt=1):
		"""
		Add given hyperedge-nodes to the hypergraph.

		@attention: While hyperedge-nodes can be of any type, it's strongly recommended to use only numbers and single-line strings as node identifiers if you intend to use write().
		
		@type  hyperedge: node
		@param hyperedge: Hyperedge-node identifier.

		@type  wt: number
		@param wt: Edge weight.
		"""
		if (not hyperedge in self.hyperedges.keys()):
			self.hyperedges[hyperedge] = []
			self.weights[hyperedge] = wt


	def add_hyperedges(self, edgelist):
		"""
		Add given hyperedge-nodes to the hypergraph.

		@attention: While hyperedge-nodes can be of any type, it's strongly recommended to use only numbers and single-line strings as node identifiers if you intend to use write().
		
		@attention: All hyperedges added by this function will have the standard weight (wt=1). Use add_hyperedge() instead if you need to set the weight to any other value.
		
		@type  edgelist: list
		@param edgelist: List of hyperedge-nodes to be added to the graph.
		"""
		for each in edgelist:
			if (not each in self.hyperedges.keys()):
				self.hyperedges[each] = []
				self.weights[each] = 1


	def add_edge(self, node, hyperedge):
		"""
		Add an edge to the hypergraph connecting given node and hyperedge-node.

		@type  node: node
		@param node: Real node.

		@type  hyperedge: node
		@param hyperedge: Hyperedge-node.
		"""
		if (hyperedge not in self.nodes[node]):
			self.nodes[node].append(hyperedge)
			self.hyperedges[hyperedge].append(node)


	def del_edge(self, node, hyperedge):
		"""
		Remove the edge linking given node and hyperedge-node from the hypergraph.

		@type  node: node
		@param node: Real node.

		@type  hyperedge: node
		@param hyperedge: Hyperedge-node.
		"""
		self.nodes[node].remove(hyperedge)
		self.nodes[hyperedge].remove(node)


	def get_edge_weight(self, node, hyperedge):
		"""
		TODO
		
		Get the weight of an arrow.

		@type  node: node
		@param node: Real node.

		@type  hyperedge: node
		@param hyperedge: Hyperedge-node.
		
		@rtype:  number
		@return: Edge weight
		"""
		pass


	def has_edge(self, node, hyperedge):
		"""
		TODO
		
		Return whether an edge linking given node and hyperedge-node exists.

		@type  node: node
		@param node: Real node.

		@type  hyperedge: node
		@param hyperedge: Hyperedge-node.

		@rtype:  boolean
		@return: Truth-value for edge existence.
		"""
		pass


	def add_hypergraph(self, graph):
		"""
		TODO
		
		Add other hypergraph to the hypergraph.
		
		@type  graph: graph
		@param graph: Graph
		"""
		pass


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
		st_, pre_, post_ = searching.depth_first_search(self, root)
		st = {}
		pre = []
		post = []
		
		nodes = self.get_nodes(hyperedge=False)
		hyperedges = self.get_nodes(real=False)
		
		for each in st_.keys():
			if (each in nodes):
				if (st_[each] in nodes or st_[each] == None):
					st[each] = st_[each]
				else:
					st[each] = st_[st_[each]]

		for i in xrange(len(pre_)):
			if (pre_[i] in nodes):
				pre.append(pre_[i])
			if (post_[i] in nodes):
				post.append(post_[i])
		
		return st, pre, post


	def breadth_first_search(self, root=None):
		"""
		TODO
		
		Breadth-first search.

		@type  root: node
		@param root: Optional root node (will explore only root's connected component)

		@rtype:  dictionary
		@return: Generated spanning tree
		"""
		pass


	def accessibility(self):
		"""
		TODO
		
		Accessibility matrix (transitive closure).

		@rtype:  dictionary
		@return: Accessibility information for each node.
		"""
		pass


	def mutual_accessibility(self):
		"""
		TODO
		
		Mutual-accessibility matrix (strongly connected components).

		@rtype:  list
		@return: Mutual-accessibility information for each node.
		"""
		pass


	def topological_sorting(self):
		"""
		TODO
		
		Topological sorting.

		@attention: Topological sorting is meaningful only for directed acyclic graphs.

		@rtype:  list
		@return: Topological sorting for the graph.
		"""
		pass


	def connected_components(self):
		"""
		TODO
		
		Connected components.

		@attention: Indentification of connected components is meaningful only for non-directed graphs.

		@rtype:  dictionary
		@return: Pairing that associates each node to its connected component.
		"""
		pass


	def minimal_spanning_tree(self, root=None):
		"""
		TODO
		
		Minimal spanning tree.

		@type  root: node
		@param root: Optional root node (will explore only root's connected component)

		@attention: Minimal spanning tree meaningful only for weighted graphs.

		@rtype:  list
		@return: Generated spanning tree.
		"""
		pass


	def shortest_path(self, source):
		"""
		TODO
		
		Return the shortest path distance between source node and all other nodes using Dijkstra's algorithm.
		
		@attention: All weights must be nonnegative.

		@type  source: node
		@param source: Node from which to start the search.

		@rtype:  tuple
		@return: A tuple containing two dictionaries, each keyed by target nodes.
			1. Shortest path spanning tree (each key points to previous node in the shortest path transversal)
			2. Shortest distance from given source to each target node
		Inaccessible target nodes do not appear in either dictionary.
		"""
		pass
	
	
	def cut_edges(self):
		"""
		TODO
		
		Return the cut-edges of the given graph.
		
		@rtype:  list
		@return: List of cut-edges.
		"""
		pass


	def cut_nodes(self):
		"""
		TODO
		
		Return the cut-nodes of the given graph.
		
		@rtype:  list
		@return: List of cut-nodes.
		"""
		pass
