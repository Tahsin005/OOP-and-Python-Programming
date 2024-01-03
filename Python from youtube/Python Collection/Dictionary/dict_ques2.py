'''Given a string and a number N, we need to mirror
the characters from the N-th position up to the length of the string in alphabetical order. In mirror operation, we change 'a' to 'z' and 'b' to 'y' and so on

input:  N = 3
        paradox
output: paizwlc

input:  N = 6
        pneumonia
output: pneumlmrz
'''
n = 3
s = "paradox"

s1 = s[0: n - 1]
s2 = s[n - 1:]

# print(s,s1,s2, end = " ")

'''Doing this in a bad...very bad way'''

# mirror = {
#     "a" :"z",  
#     "b" :"y",
#     "c" :"x",
#     "d" :"w",
#     "e" :"v",
#     "f" :"u",
#     "g" :"t",
#     "h" :"s",
#     "i" :"r",
#     "j" :"q",
#     "k" :"p",
#     "l" :"o",
#     "m" :"n",
#     "n" :"m",
#     "o" :"l",
#     "p" :"k",
#     "q" :"j",
#     "r" :"i",
#     "s" :"h",
#     "t" :"g",
#     "u" :"f",
#     "v" :"e",
#     "w" :"d",
#     "x" :"c",
#     "y" :"b",
#     "z" :"a"
# }
# ans = ""
# print(len(s2))
# for i in range(len(s2)):
#     ans += mirror[s2[i]]

# final_ans = s1 + ans
# print(final_ans)


'''Now in optimized way'''

m1 = "abcdefghijklmnopqrstuvwxyz"
# m2 = "zyxwvutsrqponmlkjihgfedcba"
m2 = m1[::-1]

mirror = dict(zip(m1,m2))
'''here we used zip() function to creat a dict
from string (can also do it in differenet iterable
like)'''
# print(mirror)

string = ""
for i in range(0,len(s2)):
    string += mirror[s2[i]]
    # print(x,y)
final_string = s1 + string
print(final_string)
