#Python Types
#Strings
print('#Strings#')
spam = 'abcd'
#print a, d
print(spam[0])
print(spam[3])


# print True
print('a' in spam)

#print False
print('a' not in spam)

#print 4, which is the length of the string
print(len(spam))

#Numbers
print('\n#Numbers#')
spam = 2.5
egg = 2

#print 5
print(spam * egg)

#print 1.25
print(spam / egg)

#print 0 (y//x) = Floor(y/x) 
print(egg // spam)

#Boolean
print('\n#Boolean#')
spam = True
egg = False

print(spam)
print(egg)

#List
print('\n#List# is a collection which is ordered and changeable. Allows duplicate members.')
spam = [10, 25, 63, 104]
egg = ['a', 'q', 'blah']

#print 10, q
print(spam[0])
print(egg[1])

spam.append(22)
print(spam)

#Dictionary
print('\n#Dictionary# is a collection which is ordered** and changeable. No duplicate members.')
print('**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.\n')
_dict = {
    'a': 'Down by the bay',
    'b': 'where the watermelon grows'
}
#print down by the bay
print(_dict['a'])

#print where the wwatermelon grows
print(_dict.get('b'))

#print none
print(_dict.get('c'))

#print all content of _dict
print(_dict.items())

#add items to dicitionary
_dict['c']= 'back to my home'
print(_dict['c'])

#Tuples
print('\nTupples# is a collection which is ordered and unchangeable. Allows duplicate members.')

spam =('a', 'b')
egg = ('c', 'd')

#add tupples and print ('a', 'b', 'c', 'd')
print(spam+egg)

_list = [5,6,7,8]
_tuple = (_list)
print(min(_tuple))
print(max(_tuple))
print(len(_tuple))

#Sets
print('\nSets is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.')
print('*Set items are unchangeable, but you can remove and/or add items whenever you like.\n')

#convert list to set
spam =  ['a','a','b','c', 'c']
spam = set(spam)
print(spam)

spam.add('d')
spam.add('e')
print(spam)

spam.remove('c')
spam.remove('e')
print(spam)