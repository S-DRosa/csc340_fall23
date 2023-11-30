# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation


class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v):

		# Create a set to store visited vertices
		visited = set()

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)
  # This code is contributed by Neelam Yadav

  	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			print(s, end=" ")

			# Get all adjacent vertices of the
			# dequeued vertex s. If a adjacent
			# has not been visited, then mark it
			# visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

# Driver's code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 7)
g.addEdge(0, 14)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(1, 5)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(2, 5)
g.addEdge(2, 6)
g.addEdge(3, 2)
g.addEdge(3, 6)
g.addEdge(3, 17)
g.addEdge(4, 4)
g.addEdge(5, 1)
g.addEdge(5, 2)
g.addEdge(5, 9)
g.addEdge(6, 2)
g.addEdge(6, 3)
g.addEdge(6, 9)
g.addEdge(6, 10)
g.addEdge(7, 0)
g.addEdge(7, 14)
g.addEdge(8, 9)
g.addEdge(9, 5)
g.addEdge(9, 6)
g.addEdge(9, 8)
g.addEdge(9, 12)
g.addEdge(9, 13)
g.addEdge(10, 6)
g.addEdge(10, 13)
g.addEdge(11, 12)
g.addEdge(11, 14)
g.addEdge(11, 15)
g.addEdge(12, 9)
g.addEdge(12, 11)
g.addEdge(12, 13)
g.addEdge(12, 15)
g.addEdge(12, 16)
g.addEdge(13, 9)
g.addEdge(13, 10)
g.addEdge(13, 12)
g.addEdge(14, 0)
g.addEdge(14, 7)
g.addEdge(14, 11)
g.addEdge(14, 15)
g.addEdge(15, 11)
g.addEdge(15, 12)
g.addEdge(15, 14)
g.addEdge(15, 16)
g.addEdge(15, 17)
g.addEdge(16, 12)
g.addEdge(16, 15)
g.addEdge(16, 17)
g.addEdge(17, 13)
g.addEdge(17, 16)
g.addEdge(17, 15)


print("Following is BFS from (starting from vertex 0)")
g.DFS(0)
