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
Cycle detection algorithms.

@sort: find_cycle
"""


def find_cycle(graph, directed=False):
    """
    Find a cycle in the given graph.
    
    This function will return a list of nodes which form a cycle in the graph or an empty list if
    no cycle exists.
    
    @type graph: graph
    @param graph: Graph.
    
    @rtype: list
    @return: List of nodes. 
    """
    
    def find_ancestors(anclist, node):
        """
        Build the of ancestors of the given node.
        """
        if (node is not None):
             anclist.append(node)
             find_ancestors(anclist, st[node])
    
    def find_cycle_to_ancestor(node, ancestor):
        """
        Find a cycle containing both node and ancestor.
        """
        path = []
        while (node != ancestor):
            path.append(node)
            node = st[node]
        path.append(node)
        path.reverse()
        return path
    
    st, pre, post = graph.depth_first_search()
    ancestors = {}
    for each in graph:
        ancestors[each] = []
        find_ancestors(ancestors[each], each)
    
    if (not directed):
        for node in graph:
            for neighbor in graph[node]:
                if not (st[node] == neighbor or st[neighbor] == node):
                    if (neighbor in ancestors[node]):
                        return find_cycle_to_ancestor(node, neighbor)
    else:
        for node in graph:
            for neighbor in graph[node]:
                if not (st[neighbor] == node):
                    if (neighbor in ancestors[node]):
                        return find_cycle_to_ancestor(node, neighbor)
    return []