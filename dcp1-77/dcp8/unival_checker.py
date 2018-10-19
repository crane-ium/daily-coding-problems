from collections import deque

class Node(object):
    """
    Node object for a binary tree
    """
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

class BinaryTree(object):
    def __init__(self, root:Node=None):
        self.root = root

def unival_counter(tree: BinaryTree):
    """
    Return True/False whether or not the tree is unival
    """
    count = 0
    nodes = deque([])
    if tree.root:
        nodes.append(tree.root)
    while nodes:
        node = nodes.pop()
        if helper(node):
            count += 1
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
    return count

def helper(node: Node):
    """
    Recursively check the nodes that all following are unival, else return False
    """
    unival = True
    if node.left:
        if node.left.val == node.val:
            unival = helper(node.left)
        else:
            return False
    if node.right:
        if node.right.val == node.val:
            unival = helper(node.right)
        else:
            return False
    return unival

if __name__ == "__main__":
    n1 = Node(1, Node(1), Node(1))
    n = Node(0, Node(1), Node(0, n1, Node(0)))
    b = BinaryTree(n)
    print(unival_counter(b))