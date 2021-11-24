#stacks are used in memory operations
#pop [draw from top of card - using analogy from a deck of cards] 
#top or peek [look at top card]
#push [place cards on top of deck]
#size [count number of cards in the deck]
#empty [check if the deck is empty]
print('#Stack#')
stack = []
def push(a):
    stack.append(a)
    
def pop():
    
    try:
        del stack[-1]
        
    except:
        return "Empty Stack"
    
def top():
    return stack[-1]

def size():
    return len(stack)

def empty():
    return True if size() == 0 else False

print(f'Let\'s see how a stack work')
stack = ['spam', 'eggs', 'ham', 'sausage', 'beans']
print(f'\nour current stack is {stack}')
print(f'size of stack is {size()}')
print(f'\nthe topmost element is \"{top()}\" but if we \"pop()\" an element')
pop()
print(f'The new topmost element is \"{top()}\" and the stack is now {stack}')
print('\nAdd a few strings to our stack')
push('coffee')
push('tea')
push('milo')
print(f'after pushing 3 new elements, our stack is now \"{stack}\"')
print(f'\nthe stack size is now {size()}')
print(f'checking if stack is empty, the result is: {empty()}')

for i in range(size()):
    pop()
print(f'\nfor loop will pop 7 times and the emptiness check should return {empty()}')

print('\n#Queue#')
#add - add to the queue
#pop - let an element out of the queue (first item of the queue)
#size - check the length or size of the queue
#empty - check if it’s empty
#first - know what the value of the first element is
#last - know what the value of the last element is

queue = []

def add(a):
    queue.append(a)

def pop():
    try:
        del queue[0]
    except:
        return "Empty Queue"
    
def size():
    return len(queue)

def empty():
    return True if len(queue) == 0 else False

def first():
    return queue[0]

def last():
    return queue[-1]

queue = ['spam', 'egg', 'ham', 'coffee', 'tea']