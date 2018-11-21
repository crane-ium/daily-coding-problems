#Find all the paths from the root to the leaves in a binary tree

#As usual, I will comment out my thought process to help guide both myself, and anyone reading

#This seems similar to analyzing a partial ordering
# or to a Hasse Diagram that always diverges

#Let's build our tree first
class node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    #Give ourselves an easy way to expand the tree
    def insert(self, *args):
        if(not args):
            return
        if not self.val:
            self.val = args[0]
            args = args[1:]
            if not args:
                return
        for arg in args:
            if arg < self.val:
                if self.left: 
                    self.left.insert(arg)
                else:
                    self.left = node(arg)
            else:
                if self.right:
                    self.right.insert(arg)
                else:
                    self.right = node(arg)
    #Let's visualize
    def print(self):
        # We are just gonna do a print by level to build on some prior training
        print(f'{self.val},')
        from collections import deque
        nodes = deque([self.left, self.right])
        temp = deque()
        while nodes:
            node = nodes.popleft()
            print(node.val, end='')
            for child in [node.left, node.right]:
                if child:
                    temp.append(child)
            if not nodes:
                nodes = temp
                temp = deque()
                print()
            else:
                print(', ', end='')
        
    #Now that our tree is built...
    #Let's print those paths to the leaves!
    #We will use recursive calls to bring back a list of values of nodes along that path
    def get_paths(self, lst:list=[]):
        if self.left and self.right:
            # print(self.left.get_paths(lst+[self.val]), self.right.get_paths(lst+[self.val]))
            return self.left.get_paths(lst+[self.val]) + self.right.get_paths(lst+[self.val])
        elif self.left:
            return self.left.get_paths(lst+[self.val])
        elif self.right:
            return self.right.get_paths(lst+[self.val])
        else:
            return [lst+[self.val]]
        # return (lst+[self.val] if not self.left else self.left.get_paths(lst+[self.val])) + \

    
if __name__ == "__main__":
    n = node(5)
    n.insert(3, 8, 1, 9, 10,7)
    n.print()
    print(n.get_paths())