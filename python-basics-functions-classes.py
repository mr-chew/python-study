#Functions
#this is the basic make up of a function
#you can pass optional parameters by giving them a preset value
#it is cutomary to spearate words with _ in Python
print('#Functions#')

#structure of a function
def example_name(mandatory_parameter, optional_parameter=True):
    # do something here to make sure you use your parameters
    if optional_parameter:
      abc = mandatory_parameter
    else:
      abc = 'xyz'
    # return some value
    return abc

# example of a function call
print(example_name("a1b2c3"))

# returns n'th fibonacci number
print('\n#Fibonacci#')

def fibonacci(n):
    if n <=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

numseq=11
#print(fibonacci(numseq-1))

for i in range(numseq):
    print(str(i+1) +') '+ str(fibonacci(i)))
