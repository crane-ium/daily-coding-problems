"""
Prompt:

This problem was asked by Google

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into a tree
"""
from collections import deque
SEP = ' '
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node:Node) -> str:
    """Serialize a node into a string"""
    if node is None:
        return '#'
    return f'{node.val}{SEP}{serialize(node.left)}{SEP}{serialize(node.right)}'

def deserialize(string:str) -> Node:
    """Deserialize a string into a node"""
    node_strings = deque(string.split(SEP))
    nodes = deque([])
    root = Node(node_strings.popleft())
    nodes.append(root)
    left = True

    while len(node_strings) > 0:
        current_node = node_strings.popleft()
        n = None
        # if current_node == '#' and nodes[0].left is None:
        #     current_node = node_strings.popleft()
        #     if current_node == '#':
        #         nodes.popleft()
        #     else:
        #         n = Node(current_node)
        #         nodes[0].right = n
        #         nodes.popleft()
        #         nodes.appendleft(n)
        # elif current_node == '#':
        if current_node == '#':
            if not left or nodes[0].left:
                nodes.popleft()
            left = left == False
        if current_node != '#':
            n = Node(current_node)
        if n:
            if nodes[0].left or not left:
                nodes[0].right = n
                nodes.popleft()
                nodes.appendleft(n)
                left = True
            else:
                nodes[0].left = n
                nodes.appendleft(n)
                left = True
    
    return root

#The following test should pass
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(deserialize(serialize(node))))
assert deserialize(serialize(node)).left.left.val == 'left.left'
node = Node('root', Node('left', right=Node('left.right', left=Node('left.right.left'))), Node('right', left=Node('right.left'), right=Node('right.right')))
print(serialize(node))
print(serialize(deserialize(serialize(node))))