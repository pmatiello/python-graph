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



# Depht First Search

def depth_first_search(graph):
	visited = []
	spanning_tree = []

	for each in xrange(len(graph)):
		visited.append(0)
		spanning_tree.append(-1)
	
	for each in xrange(len(graph)):
		if (not visited[each]):
			__dfs__(graph, visited, spanning_tree, each)

	return {'spanning_tree': spanning_tree}


def __dfs__(graph, visited, spanning_tree, node):
	visited[node] = 1
	for each in graph.get_node(node):
		if (not visited[each]):
			spanning_tree[each] = node
			__dfs__(graph, visited, spanning_tree, each)
