"""This file declares 3 directed graphs as constants and then 3 functions to \
a) Generate a complete graph
b) compute in in-degrees for a given graph
c) calculates in-degree distributions"""

EX_GRAPH0 = {0:set([1,2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]), 9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    """Takes the number of nodes num_nodes and returns a dictionary \
    corresponding to a complete directed graph with the specified \
    number of nodes."""
    graph = {}
    for item in range(num_nodes):
        graph[item]=set()
for item2 in range(num_nodes):
    if item2 != item:
        graph[item].add(item2)
        return graph

def compute_in_degrees(digraph):
    """Takes a directed graph digraph (represented as a dictionary) \
    and computes the in-degrees for the nodes in the graph."""
    graph = {}
    for key in digraph:
        graph[key] = 0
        for key in digraph:
            for item in digraph[key]:
                graph[item] += 1
    

def in_degree_distribution(digraph):
    """ Takes a directed graph digraph (represented as a dictionary) \
    and computes the unnormalized distribution of the in-degrees of \
    the graph."""
    graph = compute_in_degrees(digraph)
    results = {}
    for key in graph:
        if graph[key] in results:
            results[graph[key]] += 1
else:
    results[graph[key]] = 1
    return results



compute_in_degrees(EX_GRAPH1)
compute_in_degrees(EX_GRAPH2)


return graph
