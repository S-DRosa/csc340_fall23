# Python3 program to for tree traversals

# A class that represents an individual node in a
# Binary Tree


## a+(b∗c)+d∗(e+f)
##  a = 1
##
##  '+' = 2
##
##  b = 3
##
##  '*' = 4
##
##  c = 5
##
##  d = 6
##
##  e = 7
##
##  f = 8



class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# then print the data of node
		print(root.val),

		# now recur on right child
		printInorder(root.right)


# Driver codey
if __name__ == "__main__":
	root = Node('+')
	
	root.left = Node('+')
	root.left.left = Node('A')
	root.left.right = Node('*')
	root.left.right.left = Node('B')
	root.left.right.right = Node('C')
	
	root.right = Node('*')
	root.right.left = Node('D')
	root.right.right = Node('+')
	root.right.right.left = Node('E')
	root.right.right.right = Node('F')

	# Function call
	print("\nInorder traversal of binary tree is")
	printInorder(root)
