from collections import deque
import random

EX_GRAPH0 = {0:[1,4,5],1:[2,6],2:[3],3:[0],4:[1],5:[2],6:[],7:[5,8,9,10],8:[7,9,10],9:[7,8,10],10:[7,8,9]}

def bfs_visited(ugraph, start_node):
	"""Takes the undirected graph ugraph and the node start_node and returns \
	the set consisting of all nodes that are visited by a breadth-first search \
	that starts at start_node"""
	q = deque()
	visited = [start_node]
	q.append(start_node)
	while len(q) > 0:
		j = q.pop()
		for node in ugraph[j]:
			if node not in visited:
				visited.append(node)
				q.append(node)
	return visited



def cc_visited(ugraph):
	"""Takes the undirected graph ugraph and returns a list of sets, where each \
	set consists of all the nodes (and nothing else) in a connected component, \
	and there is exactly one set in the list for each connected component in \
	ugraph and nothing else."""
	remaining_nodes = set([key for key in ugraph.keys()])
	cc = []
	while len(remaining_nodes) > 0:
		i = random.sample(remaining_nodes,1)[0]
		w = bfs_visited(ugraph, i)
		#print "BFS Visited: " + str(w)
		cc.append(set(w))
		#print cc
		#print "remaining_nodes before "+ str(len(remaining_nodes))
		remaining_nodes = set(remaining_nodes-set(w))
		#print "remaining_nodes after: "+ str(len(remaining_nodes))
	return cc

cc_visited(EX_GRAPH0)



def largest_cc_size(ugraph):
	"""Takes the undirected graph ugraph and returns the size (an integer) of the\
	largest connected component in ugraph."""
	paths = cc_visited(ugraph)
	max_path = 0
	for path in paths:
		if len(path) > max_path:
	 		max_path = len(path)
	return max_path

largest_cc_size(EX_GRAPH0)

