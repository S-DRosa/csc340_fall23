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


# A function to do preorder tree traversal
def printPreorder(root):

	if root:

		# First print the data of node
		print(root.val),

		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)


# Driver code
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
        print ("Preorder traversal of binary tree is")
        printPreorder(root)
