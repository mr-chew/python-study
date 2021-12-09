#create node
class Node(object):
    def __init__(self, data=None, next=None): #initialise node
        self.data = data
        self.next = next
        
    def get_data(self): #retrieve node data
        return self.data
    
    def set_data(self, new_data): #set node data
        self.data = new_data
        
    def get_next(self): #get next node
        return self.next
    
    def set_next(self, next_node): #set link to next node
        self.next = next_node
        
#create link list
class Linked_List(object):
    def __init__(self, head=None): #initialise linked list
        self.head = head #setting which node as head (first) in the linked list
        self.size = 0
        
    def append(self,node): #append node to end of linked list
        currentNode = self.head
        while currentNode.next != None: #loop through the linked list untill we get to the last node
            currentNode = currentNode.next #exit loop when reach last node
        currentNode.next = node #set this last node to be link to new node
        self.size += 1 #increase size variable count by 1 (size method defined below)
        
    def size(self):
        return self.size #return value of size variable
    
    def search(self, value): #search for node
        currentNode = self.head
        found = False
        while not found: #not false = true, this will loop until it is found and exit loop
            if currentNode.data == value:
                found = True
                return currentNode
            elif currentNode.next:
                currentNode = currentNode.next
            else:
                return ValueError("The value is not found")
            
    def delete(self, value):
        currentNode = self.head
        if currentNode.data == value: #if first node matches the value
            self.head = currentNode.next #set the head pointer to next node
        else:
            previousNode = currentNode #keeping track of previous node
            currentNode = currentNode.next
            while (currentNode): #loop through the linked list
                if currentNode.data == value:                 
                    self.size -= 1
                    previousNode.next = currentNode.next #unlink the node from the linked list
                    return currentNode
                elif currentNode.next:
                    previousNode = currentNode
                    currentNode = currentNode.next
                else:
                    return ValueError("The value is not found")
  
    def traverse(self):
        currentNode = self.head
        arrayNode = [currentNode.data]
        while currentNode.next:
            currentNode = currentNode.next
            arrayNode.append(currentNode.data)
        return arrayNode
        
node1 = Node("A")
node2 = Node("Bb")
node3 = Node("Ccc")
node4 = Node("Dddd")
node5 = Node("Eeeee")


ll = Linked_List(node1)
ll.append(node2)
ll.append(node3)
ll.append(node4)
ll.append(node5)

ll.delete('Eeeee')
print(f"Current linked list is {ll.traverse()}")

print(f"Now the data of node1 is {node1.get_data()}")
node1.set_data("AAAAAAAA")
print(f"Now the data of node1 is {node1.get_data()}")

print(f"Now the size of the linked list is {ll.size}")
print(f"If we search for Ccc111, we should see that it is not in the list: {ll.search('Ccc111')}")
print(f"We should now get a response for searching for Ccc: {ll.search('Ccc')}")