def bubble_sort(rndlist):
    n = len(rndlist)
    for i in range(n-1):
        for j in range(0, n-i-1):
            print(f"comparing rndlist[{j}] and rndlist[{j+1}]")
            print(f"the value in rndlist[{j}] -> {rndlist[j]}")
            print(f"the value in rndlist[{j+1} -> {rndlist[j+1]}]")
            if rndlist[j] > rndlist[j+1]:
                print(f"rndlist[{j}] is larger -> swapping the value")
                rndlist[j], rndlist[j+1] = rndlist[j+1], rndlist[j]
                print(f"the new rndlist[] is {rndlist}")
                
rndlist = list(map(int, input("Enter a list of numbers delimited by space ").split()))
print(f"initial list is {rndlist} \n")
bubble_sort(rndlist)
print(f"final sorted list is {rndlist}")

