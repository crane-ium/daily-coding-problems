#Given a binary tree
#Find the smallest weighted path from root to a leaf

class tree(object):
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = tree(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = tree(val)
    def insert_list(self, arr):
        for it in arr:
            self.insert(it)

def print_tree(obj:tree):
    levellist = [obj] #List containing all the nodes at that level
    templist = []
    while(levellist):
        for node in levellist:
            if node == None:
                print("X", end='')
            else:
                print(f"{node.val}", end='')
                templist.append(node.left)
                templist.append(node.right)
            print(', ', end = '')
        print() #endl
        levellist = templist
        templist = []

def min_path(obj:tree):
    #If you only want it to return the path, use next line:
    #return min_node(tree)[1]
    return min_node(obj)

def min_node(obj:tree):
    #Returns the value of the minimum path from root to leaf in a tree
    #Recurse through the tree to get the minimum
    children = []
    if obj.left:
        children.append(min_node(obj.left))
    if obj.right:
        children.append(min_node(obj.right))
    #Get tuple with weight and path vertices
    min_tuple = min(children, default=(0, []), key=lambda x: x[0])
    #Return
    return (min_tuple[0]+obj.val, [obj.val]+min_tuple[1])

if __name__ == "__main__":
    mytree = tree(10, tree(5, right=tree(2)), tree(5, right=tree(1, tree(-1))))
    print_tree(mytree)
    print(f'Minimum path: {min_path(mytree)}')