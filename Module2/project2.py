"""
These are the functions for Module 2, including: \
1) bfs_visited
2) cc_visited
3) largest_cc_size
4) compute_resilience
"""
from collections import deque
import random

def bfs_visited(ugraph, start_node):
	"""Takes the undirected graph ugraph and the node start_node and returns \
	the set consisting of all nodes that are visited by a breadth-first search \
	that starts at start_node"""
	queue = deque()
	visited = set([start_node])
	queue.append(start_node)
	while len(queue) > 0:
		dequeued = queue.pop()
		for node in ugraph[dequeued]:
			if node not in visited:
				visited = list(visited)
				visited.append(node)
				visited = set(visited)
				queue.append(node)
	return visited

def cc_visited(ugraph):
	"""Takes the undirected graph ugraph and returns a list of sets, where each \
	set consists of all the nodes (and nothing else) in a connected component, \
	and there is exactly one set in the list for each connected component in \
	ugraph and nothing else."""
	remaining_nodes = set([key for key in ugraph.keys()])
	components = []
	while len(remaining_nodes) > 0:
		node = random.sample(remaining_nodes,1)[0]
		nodes_visited = bfs_visited(ugraph, node)
		#print "BFS Visited: " + str(w)
		components.append(set(nodes_visited))
		#print cc
		#print "remaining_nodes before "+ str(len(remaining_nodes))
		remaining_nodes = set(remaining_nodes-set(nodes_visited))
		#print "remaining_nodes after: "+ str(len(remaining_nodes))
	return components

def largest_cc_size(ugraph):
	"""Takes the undirected graph ugraph and returns the size (an integer) of the\
	largest connected component in ugraph."""
	paths = cc_visited(ugraph)
	max_path = 0
	for path in paths:
		if len(path) > max_path:
	 		max_path = len(path)
	return max_path

def remove_nodes(graph, nodes):
	"""Receives an undirected graph and returns said graph without nodes and edges \
	included in nodes"""
	new_graph = {}
	for node in graph:
			if node not in nodes:
				new_graph[node]=[edge for edge in graph[node] if edge not in nodes]
	return new_graph
			
def compute_resilience(ugraph, targets):
	"""implement a function that takes an undirected graph and a list of nodes \
	that will be attacked. You will remove these nodes (and their edges) from the\
	graph one at a time and then measure the "resilience" of the graph at each \
	removal by computing the size of its largest remaining connected component"""
	results = []
	results.append(largest_cc_size(ugraph))
	for number in range(len(targets)):
		nodes = targets[0:number+1]
		new_graph = remove_nodes(ugraph, nodes)
		max_path = largest_cc_size(new_graph)
		results.append(max_path)
	return results






