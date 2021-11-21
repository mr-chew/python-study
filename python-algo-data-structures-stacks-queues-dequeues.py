#stacks are used in memory operations
#pop [draw from top of card - using analogy from a deck of cards] 
#top or peek [look at top card]
#push [place cards on top of deck]
#size [count number of cards in the deck]
#empty [check if the deck is empty]

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

