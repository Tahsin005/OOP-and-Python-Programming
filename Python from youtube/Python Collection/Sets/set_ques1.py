'''Given three arrays, we have to find common elements in three sorted lists using sets
input: ar1 = [1,5,10,20,40,80]
       ar2 = [6,7,20,80,100]
       ar3 = [3,4,15,20,30,70,80,120]
output: [80,20]

input: ar1 = [1,5,5,]
       ar2 = [3,4,5,5,10]
       ar3 = [5,5,10,20]
output: [5]'''
# solution:

# ar1 = [1,5,10,20,40,80]
# ar2 = [6,7,20,80,100]
# ar3 = [3,4,15,20,30,70,80,120]
ar1 = [1,5,5,]
ar2 = [3,4,5,5,10]
ar3 = [5,5,10,20]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

# print(s1, s2, s3)
s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)

final_list = list(final_set)
print(final_list)