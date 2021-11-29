#create node
class Node(object):
    def __init__(self, data=None, next=None): #initialise node
        self.data = data
        self.next = next
        
    def get_data(self): #retrieve node data
        return self.data
    
    def set_data(self):
        self.data = new_data
        