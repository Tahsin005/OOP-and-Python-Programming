# upper() - char to uppercase
str1 = "new york"
str2 = str1.upper()
print(str2)

# lower() - char to lowercase
str3 = str2.lower()
print(str3)

# capitalize() - 1st char of each word will be capped
str4 = str3.capitalize()
print(str4)

# strip() - removes trailing whitespaces from a string
str1 = "     hello world!@      "
print(str1.strip())
# it wouldnot effect the original string
print("Original string :", str1)


'''replace() function'''
# syntax: replace(old_substring, new_substring, count)
# ** if count not given, it will replace all the occurences from that string, otherwise will only delete the given number of substrigns , starting from the first
s = "hello world tahsin ferdous. tahsin hello world tahsin tahsin"
print(s.replace("tahsin", "cubox"))
print(s.replace("tahsin", "cubox", 1))



'''split function'''
# used to split the string into a list of substrings
# by default the separator is whitespace
# string.split(sep, maxsplit)
# sep - the separator, maxsplit - number of time you want to split
s = "apple banana mango"
# string = s.split("n", 8) # parameters are optional
string = s.split() # without any argument, means would separate based on whitespace
print(string)



# concatenation
temp1 = "hello"
temp2 = " World"
print(temp1 + temp2)


# format()
# used to insert variables in a string
name = "tahsin"
id = 1068

string = "The student name is {s}, and id is {m}".format(s = name, m = id)
print(string)
