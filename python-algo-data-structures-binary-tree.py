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

#The anchor step here is check that either the left or right child exists. 
#If it doesn’t, then a new Node is attached to the tree and no further recursive call is made.        
    def append(self, node): 
        _val = node.val
        if _val <= self.val:
            if self.left: #this condition is true if there is left child to existing node
                # print(f"left child node {self.left.val} exist, recursive call append({_val}) again")
                self.left.append(node)
            else:
                # print(f"new left node({_val}) is attached to node {self.val}")
                self.left = node
                # print(f"print left node value ===> {node.val}")
        else:
            if self.right: #this condition is true if there is right child to existing node
                # print(f"right child node {self.right.val} exist, recursive call append({_val}) again")
                self.right.append(node)
            else:
                # print(f"new right node({_val}) is attached to node {self.val}")
                self.right = node
                # print(f"print right node value ===> {node.val}")
                
    def search(self,val):
        if val == self.val:
            return True
        if val <= self.val and self.left: #value to find is smaller than current node value + left child node exist
            self.left.search(val)
        elif val > self.val and self.right: #value to find is larger than current node value + right child node exist
            self.right.search(val)
        else:
            print("Value could not be found")
            return False
    
    # return the parent node and successor        
    def find_successor(self, parent):
        if self.left:
            print(f"self > {self.val} self.left > {self.left.val} parent > {parent.val}")
            return self.left.find_successor(self)
        else:
            print(f"P is {parent.val}, S is {self.val}")
            return parent, self
    
    def delete(self, val):
        print(f"current node value {self.val}")
        print(f"Deleting {val} if it exist")
        if self.val == val:
            if self.right and self.left:
                print(f"--->>>>>left node {self.left.val} right node is {self.right.val} self node is {self.val}")
                parent, successor = self.right.find_successor(self)
                print(f"<<<<<<---parent node {parent.val} successor node is {successor.val}")
                # split out the successor
                if parent.left == successor:
                    print(f"<<<-parent.left {parent.left.val} successor {successor.val} {successor.right}")
                    parent.left = successor.right
                else:
                    # print(f"<<<-parent.right {parent.right.val} successor.right {successor.right.val}")
                    parent.right = successor.right
                # set left and right nodes of the successor [i.e. replace node to be deleted]
                # print(f"{self.left.val} {self.right.val}")
                successor.left = self.left
                successor.right = self.right
                return successor
            else:
                if self.left:
                    return self.left
                else:
                    return self.right
        else:
            if self.val > val:
                if self.left:
                    print(f"<<<<<< traverse down to left child node {self.left.val}")
                    self.left = self.left.delete(val)
            else:
                if self.right:
                    print(f">>>>> traverse down to right child node")
                    self.right = self.right.delete(val)
        # print(f"node not found at {self.val}")
        return self
    
    def inorder_print(self):
        if self.left:
            self.left.inorder_print()
        print(f"{self.val}")
        if self.right:
            self.right.inorder_print()
            
root = BinaryTree(5)
root.append_val(2)
root.append_val(8)
root.append_val(3)
root.append_val(1)
root.append_val(10)
root.append_val(7)
root.append_val(6)
root.append_val(4)
# print('\n')

root.inorder_print()

# root.find_successor(7)
root = root.delete(5)
# root.delete(8)
print('\n')
root.inorder_print()