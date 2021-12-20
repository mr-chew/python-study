def heap(rndlist, n, i):
    print(f"heaping on index {i}")
    parent = i
    leftc = 2*i + 1
    rightc = 2*i + 2
    # n here refer to size of rndlist
    # if left child node of parent exists and
    # is greater than parent node
    if leftc < n and rndlist[leftc] > rndlist[parent]:
        print(f"swaping left child node -> {rndlist[leftc]} and parent node {rndlist[parent]}")
        parent = leftc #actual swap happen few lines below
    # if left child node of parent exists and
    # is greater than parent node    
    if rightc < n and rndlist[rightc] > rndlist[parent]:
        print(f"swapping right child node -> {rndlist[rightc]} and parent node {rndlist[parent]}")
        parent = rightc
    # actual begin here
    if parent != i:
        rndlist[i], rndlist[parent] = rndlist[parent], rndlist[i]
        print(f"new list is now {rndlist} \n")
        # continue to build the max heap
        heap(rndlist, n, parent)
        
def heap_sort(rndlist):
    n = len(rndlist)
    # example list 2, 6, 4, 9, 7, start loop from the middle 5//2 = 2 and move toward index = 0
    for i in range(n//2 - 1, -1, -1):
        heap(rndlist, n, i)
    
    #"extract" the root node [swap with last node] once max heap is form and 
    # repeat building the max heap on root node - index [0]
    for i in range(n-1, 0, -1):
        rndlist[i], rndlist[0] = rndlist[0], rndlist[i]
        heap(rndlist, i, 0)
        
unsortedlist = list(map(int, input("input numbers separated by spaces ").split()))
print(f"the initial list is {unsortedlist} \n")
heap_sort(unsortedlist)
print(f"the sorted list is {unsortedlist}")