#val refer to value of the node
#right refer to right node
#left refer to left node

class BinaryTree(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def append_val(self, val):
        self.append(BinaryTree(val))

#The anchor step here is the check that either the left or right child exists. 
#If it doesn’t, then a new Node is attached to the tree and no further recursive call is made.        
    def append(self, node): 
        _val = node.val
        if _val <= self.val:
            if self.left: #this condition is true if there is left child to existing node
                print(f"moving left to append {_val}")
                self.left.append(node)
            else:
                print(f"setting left {_val}")
                self.left = node