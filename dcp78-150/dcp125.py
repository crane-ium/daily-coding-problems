from collections import defaultdict
from collections import deque
#Given a binary tree, find two nodes in the tree whose sum is k

class node(object):
    def __init__(self, val:int=0, left=None,right=None):
        self.left = left
        self.right = right
        self.val = val
    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = node(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = node(val)
    # def 
    
def find_k_sum(root:node, k:int):
    #Return a tuple of the nodes?
    #Since we can assume our tree is a binary tree, we can search it much more efficiently
    #Let's think of possible solutions
    #We could use a dictionary to store difference between sum and the node
    #We could do in-order traversal with to find the nodes
    #We could do... 
    #For now let's go through the tree using a deque and holding values with dict
    deq = deque()
    differences = defaultdict(None)
    deq.appendleft(root)
    while(deq):
        nxt = deq.pop()
        if nxt.left:
            deq.appendleft(nxt.left)
        if nxt.right:
            deq.appendleft(nxt.right)
        if differences.get(nxt.val, None):
            return (nxt, differences[nxt.val])
        else:
            differences[k-nxt.val] = nxt
    #If reached here, no result
    return (node(0),node(0))
    
if __name__ == "__main__":
    #Let's build our tree quickly to represent the given tree
    tree = node(10, node(5), node(15, node(11), node(15)))
    nodes = find_k_sum(tree, 15)
    print(nodes[0].val, nodes[1].val)