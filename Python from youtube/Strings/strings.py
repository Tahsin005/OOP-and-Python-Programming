# Sequence of characters within '', "", ''' '''
# Immutable: cannot change the original string 
# but can manipulate that string to create another
# string

name1 = 'Mohammad'
name2 = "Tahsin"
name3 = '''Ferdous'''

print(name1, name2, name3)

# for multiline string : triple quotes

paragraph = '''This is a multiline string.
You can write multiple lines within triple quotes'''
print(paragraph)

# indexing like array / list 
hello = "Hello, World!"
print(hello[0])
print(hello[4])
print(hello[-1])

# travesing

for i in name1:
    print(i, end = " ")
print()
# ->
for i in range(len(name1)):
    print(name1[i], end= " ") 

print()
# using list comprehesion
list = [char for char in name1]
for i in list:
    print(i)

print()
# find a character / substring in a string
# returns the index of the char / index of
# the first char in looking substring
# else will return -1
print(name1.find('h'))
print(name1.find('tahsin'))

