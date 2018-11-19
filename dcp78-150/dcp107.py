from random import randint
#Printing nodes of a binary tree by level

class btree(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def insert(self, val):
        if(val < self. val):
            if self.left:
                self.left.insert(val)
            else:
                self.left = btree(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = btree(val)
    def __str__(self):
        return str(self.val)
    
def print_btree_levels(tree:btree):
    nodes = [tree] #Track that level of nodes by creating a list
    output = ''
    while(nodes):
        temp=[]
        for node in (nodes):
            output += str(node.val) + ', '
            if node.left: #Add in the nodes
                temp.append(node.left)
            if node.right: 
                temp.append(node.right)
        output += '\n' #Print neatly by seperating levels
        nodes = temp
    output = output.strip(' ,\n') #I think it's faster to just cut at the end rather than to check in-loop
    print(output)

if __name__ == "__main__":
    #Create tree
    tree = btree(3)
    lst = [1, 2, 5, 4, 6, 7 ,0]
    for l in lst:
        tree.insert(l) #Insert into the tree
    print_btree_levels(tree)